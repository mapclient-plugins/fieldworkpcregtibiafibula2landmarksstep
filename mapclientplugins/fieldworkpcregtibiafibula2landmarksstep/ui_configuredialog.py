# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(545, 384)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.configGroupBox = QGroupBox(Dialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.lineEdit0 = QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName(u"lineEdit0")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit0)

        self.label_5 = QLabel(self.configGroupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.lineEditMC = QLineEdit(self.configGroupBox)
        self.lineEditMC.setObjectName(u"lineEditMC")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditMC)

        self.label = QLabel(self.configGroupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.lineEditLC = QLineEdit(self.configGroupBox)
        self.lineEditLC.setObjectName(u"lineEditLC")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEditLC)

        self.label_3 = QLabel(self.configGroupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.lineEditMM = QLineEdit(self.configGroupBox)
        self.lineEditMM.setObjectName(u"lineEditMM")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEditMM)

        self.label_2 = QLabel(self.configGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.lineEditLM = QLineEdit(self.configGroupBox)
        self.lineEditLM.setObjectName(u"lineEditLM")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEditLM)

        self.label_4 = QLabel(self.configGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.lineEditTT = QLineEdit(self.configGroupBox)
        self.lineEditTT.setObjectName(u"lineEditTT")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEditTT)

        self.label_6 = QLabel(self.configGroupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_6)

        self.lineEditKC = QLineEdit(self.configGroupBox)
        self.lineEditKC.setObjectName(u"lineEditKC")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEditKC)

        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label0)

        self.label_8 = QLabel(self.configGroupBox)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_8)

        self.doubleSpinBox = QDoubleSpinBox(self.configGroupBox)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.doubleSpinBox)

        self.label_7 = QLabel(self.configGroupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_7)

        self.checkBoxGUI = QCheckBox(self.configGroupBox)
        self.checkBoxGUI.setObjectName(u"checkBoxGUI")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.checkBoxGUI)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        QWidget.setTabOrder(self.lineEdit0, self.lineEditMC)
        QWidget.setTabOrder(self.lineEditMC, self.lineEditLC)
        QWidget.setTabOrder(self.lineEditLC, self.lineEditMM)
        QWidget.setTabOrder(self.lineEditMM, self.lineEditLM)
        QWidget.setTabOrder(self.lineEditLM, self.lineEditTT)
        QWidget.setTabOrder(self.lineEditTT, self.lineEditKC)
        QWidget.setTabOrder(self.lineEditKC, self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Configure Tibia Fibula Registration Step", None))
        self.configGroupBox.setTitle("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Medial Epicondyle:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Lateral Epicondyle:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Medial Maleolus:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Lateral Maleolus:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Tibial Tuberosity:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Knee Centre:", None))
        self.label0.setText(QCoreApplication.translate("Dialog", u"identifier:  ", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Marker Correction:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"GUI:", None))
        self.checkBoxGUI.setText("")
    # retranslateUi

