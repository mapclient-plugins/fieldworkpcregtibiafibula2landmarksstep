# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/configuredialog.ui'
#
# Created: Mon Jul 13 12:00:35 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(545, 240)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.configGroupBox = QtGui.QGroupBox(Dialog)
        self.configGroupBox.setTitle("")
        self.configGroupBox.setObjectName("configGroupBox")
        self.formLayout = QtGui.QFormLayout(self.configGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label0 = QtGui.QLabel(self.configGroupBox)
        self.label0.setObjectName("label0")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label0)
        self.lineEdit0 = QtGui.QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName("lineEdit0")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit0)
        self.label_2 = QtGui.QLabel(self.configGroupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditLM = QtGui.QLineEdit(self.configGroupBox)
        self.lineEditLM.setObjectName("lineEditLM")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditLM)
        self.label_3 = QtGui.QLabel(self.configGroupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEditMM = QtGui.QLineEdit(self.configGroupBox)
        self.lineEditMM.setObjectName("lineEditMM")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditMM)
        self.label_4 = QtGui.QLabel(self.configGroupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEditTT = QtGui.QLineEdit(self.configGroupBox)
        self.lineEditTT.setObjectName("lineEditTT")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditTT)
        self.label_7 = QtGui.QLabel(self.configGroupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_7)
        self.checkBoxGUI = QtGui.QCheckBox(self.configGroupBox)
        self.checkBoxGUI.setText("")
        self.checkBoxGUI.setObjectName("checkBoxGUI")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.checkBoxGUI)
        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit0, self.lineEditLM)
        Dialog.setTabOrder(self.lineEditLM, self.lineEditMM)
        Dialog.setTabOrder(self.lineEditMM, self.lineEditTT)
        Dialog.setTabOrder(self.lineEditTT, self.checkBoxGUI)
        Dialog.setTabOrder(self.checkBoxGUI, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Configure Tibia Fibula Registration Step", None, QtGui.QApplication.UnicodeUTF8))
        self.label0.setText(QtGui.QApplication.translate("Dialog", "identifier:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Lateral Maleolus", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Medial Maleolus", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Tibia Tuberosity", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "GUI:", None, QtGui.QApplication.UnicodeUTF8))

