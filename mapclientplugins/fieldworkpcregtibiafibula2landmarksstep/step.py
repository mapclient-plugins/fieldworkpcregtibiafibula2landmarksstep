
'''
MAP Client Plugin Step
'''
import os
import json
import copy

from PySide import QtGui

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.fieldworkpcregtibiafibula2landmarksstep.configuredialog import ConfigureDialog
from mapclientplugins.fieldworkpcregtibiafibula2landmarksstep.pcregviewerwidget import MayaviPCRegViewerWidget

from gias.musculoskeletal import model_alignment as ma
from gias.common import math
from mappluginutils.datatypes import transformations
import numpy as np


TIBFIBLANDMARKS = ('LM', 'MM', 'TT', 'LC', 'MC', 'kneecentre')

class FieldworkPCRegPelvis2LandmarksStep(WorkflowStepMountPoint):
    '''
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    '''

    _pcfitmw0 = 1e2
    _pcfitmwn = 1e2

    def __init__(self, location):
        super(FieldworkPCRegPelvis2LandmarksStep, self).__init__('Fieldwork PC-Reg Tibia-Fibula 2 Landmarks', location)
        self._configured = False # A step cannot be executed until it has been configured.
        self._category = 'Registration'
        # Add any other initialisation code here:
        self._icon = QtGui.QImage(':/fieldworkpcregtibiafibula2landmarksstep/images/fieldworktibiafibulapcregicon.png')
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#landmarks'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'ju#principalcomponents'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'ju#fieldworkmodel'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'ju#fieldworkmodel'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'ju#geometrictransform'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'python#float'))

        self._config = {}
        self._config['identifier'] = ''
        self._config['GUI'] = True
        self._config['marker_offset'] = '10.0'
        for l in TIBFIBLANDMARKS:
            self._config[l] = 'none'

        self._landmarks = None
        self._pc = None
        self._inputModel = None
        self._outputModel = None
        self._rmse = None
        self._transform = None

    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''
        self._inputModel.set_field_parameters(self._pc.getMean().reshape((3,-1,1)))
        if self._config['GUI']:
            print('launching registration gui')
            # model = copy.deepcopy(self._inputModel)
            self._widget = MayaviPCRegViewerWidget(self._landmarks,
                                                   self._inputModel,
                                                   self._config,
                                                   self.reg,
                                                  )
            self._widget._ui.acceptButton.clicked.connect(self._doneExecution)
            self._widget._ui.abortButton.clicked.connect(self._abort)
            self._widget.setModal(True)
            self._setCurrentWidget(self._widget)
        else:
            self.reg()
            self._doneExecution()

    def _abort(self):
        raise RuntimeError('Pelvis Landmark Registration Aborted')

    def _correctLandmarks(self):
        # move landmarks closer to centre in anterior-posterior directio
        landmarkShift = float(self._config['marker_offset'])
        if (self._config['LM']!='none') and (self._config['MM']!='none'):
            centreAnkle = 0.5*(self._landmarks[self._config['LM']] + self._landmarks[self._config['MM']])
            vMedialLateral = math.norm(self._landmarks[self._config['LM']] - self._landmarks[self._config['MM']])
            self._landmarks[self._config['LM']] -= landmarkShift*vMedialLateral
            self._landmarks[self._config['MM']] += landmarkShift*vMedialLateral

            if self._config['TT']!='none':
                vAntPost = math.norm(np.cross(vMedialLateral, self._landmarks[self._config['TT']]))
                self._landmarks[self._config['TT']] += landmarkShift*vAntPost

        if (self._config['LC']!='none') and (self._config['MC']!='none'):
            print self._config['LC']
            print self._config['MC']
            centrePlat = 0.5*(self._landmarks[self._config['LC']] + self._landmarks[self._config['MC']])
            vMedialLateral = math.norm(self._landmarks[self._config['LC']] - self._landmarks[self._config['MC']])
            self._landmarks[self._config['LC']] -= landmarkShift*vMedialLateral
            self._landmarks[self._config['MC']] += landmarkShift*vMedialLateral

            if self._config['TT']!='none':
                vAntPost = math.norm(np.cross(vMedialLateral, self._landmarks[self._config['TT']]))
                self._landmarks[self._config['TT']] += landmarkShift*vAntPost

    def reg(self, callbackSignal=None):

        if callbackSignal is not None:
            def callback(output):
                callbackSignal.emit(output)
        else:
            callback = None

        self._correctLandmarks()
        inputLandmarks = [(l, self._landmarks[self._config[l]]) for l in TIBFIBLANDMARKS if self._config[l]!='none']
        
        self._outputModel,\
        alignmentSSE,\
        T = ma.alignTibiaFibulaLandmarksPC(self._inputModel,
                                      self._pc,
                                      inputLandmarks,
                                      GFParamsCallback=callback,
                                      mw0=self._pcfitmw0,
                                      mwn=self._pcfitmwn)

        self._rmse = np.sqrt(alignmentSSE[2]/len(inputLandmarks))
        self._transform = transformations.RigidPCModesTransform(T)
        return self._outputModel, self._rmse, T

    def setPortData(self, index, dataIn):
        '''
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.
        '''
        if index==0:
            self._landmarks = dataIn # ju#landmarks
        elif index==1:
            self._pc = dataIn
        else:
            self._inputModel = dataIn

    def getPortData(self, index):
        '''
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        '''
        if index==3:
            return self._outputModel # ju#landmarks
        elif index==4:
            return self._transform
        else:
            return self._rmse

    def configure(self):
        '''
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        '''
        dlg = ConfigureDialog()
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)
        
        if dlg.exec_():
            self._config = dlg.getConfig()
        
        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        '''
        The identifier is a string that must be unique within a workflow.
        '''
        return self._config['identifier']

    def setIdentifier(self, identifier):
        '''
        The framework will set the identifier for this step when it is loaded.
        '''
        self._config['identifier'] = identifier

    def serialize(self):
        '''
        Add code to serialize this step to disk. Returns a json string for
        mapclient to serialise.
        '''
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        '''
        Add code to deserialize this step from disk. Parses a json string
        given by mapclient
        '''
        self._config.update(json.loads(string))

        # for config from older versions
        if self._config['GUI']=='True':
            self._config['GUI'] = True
        else:
            self._config['GUI'] = False

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()


