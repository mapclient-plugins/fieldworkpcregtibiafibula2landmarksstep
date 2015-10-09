'''
MAP Client, a program to generate detailed musculoskeletal models for OpenSim.
    Copyright (C) 2012  University of Auckland
    
This file is part of MAP Client. (http://launchpad.net/mapclient)

    MAP Client is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    MAP Client is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with MAP Client.  If not, see <http://www.gnu.org/licenses/>..
'''
import os
os.environ['ETS_TOOLKIT'] = 'qt4'

from PySide.QtGui import QDialog, QFileDialog, QDialogButtonBox,\
                         QAbstractItemView, QTableWidgetItem
from PySide.QtGui import QDoubleValidator, QIntValidator
from PySide.QtCore import Qt
from PySide.QtCore import QThread, Signal

from mapclientplugins.fieldworkpcregtibiafibula2landmarksstep.ui_pcregviewerwidget import Ui_Dialog
from traits.api import HasTraits, Instance, on_trait_change, \
    Int, Dict

from mappluginutils.mayaviviewer import MayaviViewerObjectsContainer,\
                                        MayaviViewerLandmark,\
                                        MayaviViewerFieldworkModel,\
                                        colours
import numpy as np
import copy

class _ExecThread(QThread):
    finalUpdate = Signal(tuple)
    update = Signal(tuple)

    def __init__(self, func):
        QThread.__init__(self)
        self.func = func

    def run(self):
        output = self.func(self.update)
        self.finalUpdate.emit(output)

class MayaviPCRegViewerWidget(QDialog):
    '''
    Configure dialog to present the user with the options to configure this step.
    '''
    defaultColor = colours['bone']
    objectTableHeaderColumns = {'Visible':0}
    backgroundColour = (0.0,0.0,0.0)
    _modelRenderArgs = {}
    _modelDisc = [10,10]
    _landmarkRenderArgs = {'mode':'sphere', 'scale_factor':20.0, 'color':(0,1,0)}

    def __init__(self, landmarks, model, config, regFunc, parent=None):
        '''
        Constructor
        '''
        QDialog.__init__(self, parent)
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        self._scene = self._ui.MayaviScene.visualisation.scene
        self._scene.background = self.backgroundColour

        self.selectedObjectName = None
        self._landmarks = landmarks
        self._landmarkNames = ['none',]
        self._landmarkNames = self._landmarkNames + sorted(self._landmarks.keys())
        self._origModel = model
        self._regFunc = regFunc
        self._config = config

        self._worker = _ExecThread(self._regFunc)
        self._worker.finalUpdate.connect(self._regUpdate)
        self._worker.update.connect(self._updateMeshGeometry)

        # print 'init...', self._config

        ### FIX FROM HERE ###
        # create self._objects
        self._initViewerObjects()
        self._setupGui()
        self._makeConnections()
        self._initialiseObjectTable()
        self._initialiseSettings()
        self._refresh()

        self._modelRow = None

        # self.testPlot()
        # self.drawObjects()
        print('finished init...', self._config)

    def _initViewerObjects(self):
        self._objects = MayaviViewerObjectsContainer()
        self._objects.addObject('tibia-fibula mesh',
                                MayaviViewerFieldworkModel('tibia-fibula mesh',
                                                           copy.deepcopy(self._origModel),
                                                           self._modelDisc,
                                                           renderArgs=self._modelRenderArgs
                                                           )
                                )
        # 'none' is first elem in self._landmarkNames, so skip that
        for ln in self._landmarkNames[1:]:
            self._objects.addObject(ln, MayaviViewerLandmark(ln,
                                                             self._landmarks[ln],
                                                             renderArgs=self._landmarkRenderArgs
                                                             )
                                    )
        
    def _setupGui(self):
        self._ui.screenshotPixelXLineEdit.setValidator(QIntValidator())
        self._ui.screenshotPixelYLineEdit.setValidator(QIntValidator())
        for l in self._landmarkNames:
            self._ui.comboBoxLC.addItem(l)
            self._ui.comboBoxMC.addItem(l)
            self._ui.comboBoxLM.addItem(l)
            self._ui.comboBoxMM.addItem(l)
            self._ui.comboBoxTT.addItem(l)
            self._ui.comboBoxKC.addItem(l)

    def _makeConnections(self):
        self._ui.tableWidget.itemClicked.connect(self._tableItemClicked)
        self._ui.tableWidget.itemChanged.connect(self._visibleBoxChanged)
        self._ui.screenshotSaveButton.clicked.connect(self._saveScreenShot)
        
        self._ui.regButton.clicked.connect(self._worker.start)
        self._ui.regButton.clicked.connect(self._regLockUI)

        self._ui.resetButton.clicked.connect(self._reset)
        self._ui.abortButton.clicked.connect(self._abort)
        self._ui.acceptButton.clicked.connect(self._accept)

        self._ui.comboBoxLM.activated.connect(self._updateConfigLM)
        self._ui.comboBoxMM.activated.connect(self._updateConfigMM)
        self._ui.comboBoxTT.activated.connect(self._updateConfigTT)
        self._ui.comboBoxLC.activated.connect(self._updateConfigLC)
        self._ui.comboBoxMC.activated.connect(self._updateConfigMC)
        self._ui.comboBoxKC.activated.connect(self._updateConfigKC)

        self._ui.doubleSpinBoxMarkerOffset.valueChanged.connect(self._updateMarkerOffset)

    def _initialiseSettings(self):
        if self._config['LC'] in self._landmarkNames:
            self._ui.comboBoxLC.setCurrentIndex(self._landmarkNames.index(self._config['LC']))
        else:
            self._ui.comboBoxLC.setCurrentIndex(0)

        if self._config['MC'] in self._landmarkNames:
            self._ui.comboBoxMC.setCurrentIndex(self._landmarkNames.index(self._config['MC']))
        else:
            self._ui.comboBoxMC.setCurrentIndex(0)

        if self._config['LM'] in self._landmarkNames:
            self._ui.comboBoxLM.setCurrentIndex(self._landmarkNames.index(self._config['LM']))
        else:
            self._ui.comboBoxLM.setCurrentIndex(0)

        if self._config['MM'] in self._landmarkNames:
            self._ui.comboBoxMM.setCurrentIndex(self._landmarkNames.index(self._config['MM']))
        else:
            self._ui.comboBoxMM.setCurrentIndex(0)

        if self._config['TT'] in self._landmarkNames:
            self._ui.comboBoxTT.setCurrentIndex(self._landmarkNames.index(self._config['TT']))
        else:
            self._ui.comboBoxTT.setCurrentIndex(0)

        if self._config['kneecentre'] in self._landmarkNames:
            self._ui.comboBoxKC.setCurrentIndex(self._landmarkNames.index(self._config['kneecentre']))
        else:
            self._ui.comboBoxKC.setCurrentIndex(0)

        self._ui.doubleSpinBoxMarkerOffset.setValue(float(self._config['marker_offset']))

    def _initialiseObjectTable(self):
        self._ui.tableWidget.setRowCount(self._objects.getNumberOfObjects())
        self._ui.tableWidget.verticalHeader().setVisible(False)
        self._ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self._ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self._ui.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        
        r = 0
        # 'none' is first elem in self._landmarkNames, so skip that
        for ln in self._landmarkNames[1:]:
            self._addObjectToTable(r, ln, self._objects.getObject(ln))
            r += 1

        self._addObjectToTable(r, 'tibia-fibula mesh', self._objects.getObject('tibia-fibula mesh'), checked=True)
        self._modelRow = r
        self._ui.tableWidget.resizeColumnToContents(self.objectTableHeaderColumns['Visible'])

    def _addObjectToTable(self, row, name, obj, checked=True):
        typeName = obj.typeName
        print('adding to table: %s (%s)'%(name, typeName))
        tableItem = QTableWidgetItem(name)
        if checked:
            tableItem.setCheckState(Qt.Checked)
        else:
            tableItem.setCheckState(Qt.Unchecked)

        self._ui.tableWidget.setItem(row, self.objectTableHeaderColumns['Visible'], tableItem)

    def _tableItemClicked(self):
        selectedRow = self._ui.tableWidget.currentRow()
        self.selectedObjectName = self._ui.tableWidget.item(
                                    selectedRow,
                                    self.objectTableHeaderColumns['Visible']
                                    ).text()
        print(selectedRow)
        print(self.selectedObjectName)

    def _visibleBoxChanged(self, tableItem):
        # get name of object selected
        # name = self._getSelectedObjectName()

        # checked changed item is actually the checkbox
        if tableItem.column()==self.objectTableHeaderColumns['Visible']:
            # get visible status
            name = tableItem.text()
            visible = tableItem.checkState().name=='Checked'

            print('visibleboxchanged name', name)
            print('visibleboxchanged visible', visible)

            # toggle visibility
            obj = self._objects.getObject(name)
            print(obj.name)
            if obj.sceneObject:
                print('changing existing visibility')
                obj.setVisibility(visible)
            else:
                print('drawing new')
                obj.draw(self._scene)

    def _getSelectedObjectName(self):
        return self.selectedObjectName

    def _getSelectedScalarName(self):
        return 'none'

    def drawObjects(self):
        for name in self._objects.getObjectNames():
            self._objects.getObject(name).draw(self._scene)

    def _updateConfigLM(self):
        self._config['LM'] = self._ui.comboBoxLM.currentText()

    def _updateConfigMM(self):
        self._config['MM'] = self._ui.comboBoxMM.currentText()

    def _updateConfigLC(self):
        self._config['LC'] = self._ui.comboBoxLC.currentText()

    def _updateConfigMC(self):
        self._config['MC'] = self._ui.comboBoxMC.currentText()

    def _updateConfigTT(self):
        self._config['TT'] = self._ui.comboBoxTT.currentText()

    def _updateConfigKC(self):
        self._config['kneecentre'] = self._ui.comboBoxKC.currentText()

    def _updateMarkerOffset(self):
        self._config['marker_offset'] = str(self._ui.doubleSpinBoxMarkerOffset.value())

    def _updateMeshGeometry(self, P):
        meshObj = self._objects.getObject('tibia-fibula mesh')
        meshObj.updateGeometry(P.reshape((3,-1,1)), self._scene)

    def _regUpdate(self, output):
        regModel, RMSE, T = output
        # update error field
        self._ui.lineEditRMSE.setText('{:12.10f}'.format(RMSE))
        self._ui.lineEditTransformation.setText(', '.join(['{:5.2f}'.format(t) for t in T]))

        # unlock reg ui
        self._regUnlockUI()

    def _regLockUI(self):
        self._ui.comboBoxLC.setEnabled(False)
        self._ui.comboBoxMC.setEnabled(False)
        self._ui.comboBoxLM.setEnabled(False)
        self._ui.comboBoxMM.setEnabled(False)
        self._ui.comboBoxTT.setEnabled(False)
        self._ui.comboBoxKC.setEnabled(False)
        self._ui.doubleSpinBoxMarkerOffset.setEnabled(False)
        self._ui.regButton.setEnabled(False)
        self._ui.resetButton.setEnabled(False)
        self._ui.acceptButton.setEnabled(False)
        self._ui.abortButton.setEnabled(False)

    def _regUnlockUI(self):
        self._ui.comboBoxLC.setEnabled(True)
        self._ui.comboBoxMC.setEnabled(True)
        self._ui.comboBoxLM.setEnabled(True)
        self._ui.comboBoxMM.setEnabled(True)
        self._ui.comboBoxTT.setEnabled(True)
        self._ui.comboBoxKC.setEnabled(True)
        self._ui.doubleSpinBoxMarkerOffset.setEnabled(True)
        self._ui.regButton.setEnabled(True)
        self._ui.resetButton.setEnabled(True)
        self._ui.acceptButton.setEnabled(True)
        self._ui.abortButton.setEnabled(True)

    def _reset(self):
        # delete viewer table row
        # self._ui.tableWidget.removeRow(2)
        # reset mesh
        meshObj = self._objects.getObject('tibia-fibula mesh')
        meshObj.updateGeometry(self._origModel.get_field_parameters(), self._scene)
        # meshTableItem = self._ui.tableWidget.item(len(self._landmarkNames)-1,
        #                                           self.objectTableHeaderColumns['Visible'])
        # meshTableItem.setCheckState(Qt.Unchecked)

    def _accept(self):
        self._close()

    def _abort(self):
        self._reset()
        self._close()

    def _close(self):
        for name in self._objects.getObjectNames():
            self._objects.getObject(name).remove()

        self._objects._objects = {}
        self._objects == None

        # for r in xrange(self._ui.tableWidget.rowCount()):
        #     self._ui.tableWidget.removeRow(r)

    def _refresh(self):
        for r in range(self._ui.tableWidget.rowCount()):
            tableItem = self._ui.tableWidget.item(r, self.objectTableHeaderColumns['Visible'])
            name = tableItem.text()
            visible = tableItem.checkState().name=='Checked'
            obj = self._objects.getObject(name)
            print(obj.name)
            if obj.sceneObject:
                print('changing existing visibility')
                obj.setVisibility(visible)
            else:
                print('drawing new')
                obj.draw(self._scene)

    def _saveScreenShot(self):
        filename = self._ui.screenshotFilenameLineEdit.text()
        width = int(self._ui.screenshotPixelXLineEdit.text())
        height = int(self._ui.screenshotPixelYLineEdit.text())
        self._scene.mlab.savefig( filename, size=( width, height ) )

    #================================================================#
    @on_trait_change('scene.activated')
    def testPlot(self):
        # This function is called when the view is opened. We don't
        # populate the scene when the view is not yet open, as some
        # VTK features require a GLContext.
        print('trait_changed')

        # We can do normal mlab calls on the embedded scene.
        self._scene.mlab.test_points3d()


    # def _saveImage_fired( self ):
    #     self.scene.mlab.savefig( str(self.saveImageFilename), size=( int(self.saveImageWidth), int(self.saveImageLength) ) )
        