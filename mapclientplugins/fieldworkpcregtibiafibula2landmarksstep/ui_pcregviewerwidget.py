# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pcregviewerwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from gias3.mapclientpluginutilities.viewers.mayaviscenewidget import MayaviSceneWidget

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1263, 762)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widgetMain = QWidget(Dialog)
        self.widgetMain.setObjectName(u"widgetMain")
        self.widgetMain.setEnabled(True)
        sizePolicy.setHeightForWidth(self.widgetMain.sizePolicy().hasHeightForWidth())
        self.widgetMain.setSizePolicy(sizePolicy)
        self.widgetMain.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.widgetMain)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.widgetMain)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setMaximumSize(QSize(16777215, 150))
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)

        self.verticalLayout.addWidget(self.tableWidget)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label)

        self.comboBoxLM = QComboBox(self.widget)
        self.comboBoxLM.setObjectName(u"comboBoxLM")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.comboBoxLM)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.comboBoxMM = QComboBox(self.widget)
        self.comboBoxMM.setObjectName(u"comboBoxMM")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.comboBoxMM)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.comboBoxTT = QComboBox(self.widget)
        self.comboBoxTT.setObjectName(u"comboBoxTT")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.comboBoxTT)

        self.comboBoxMC = QComboBox(self.widget)
        self.comboBoxMC.setObjectName(u"comboBoxMC")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboBoxMC)

        self.comboBoxLC = QComboBox(self.widget)
        self.comboBoxLC.setObjectName(u"comboBoxLC")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBoxLC)

        self.comboBoxKC = QComboBox(self.widget)
        self.comboBoxKC.setObjectName(u"comboBoxKC")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.comboBoxKC)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_8)

        self.doubleSpinBoxMarkerOffset = QDoubleSpinBox(self.widget)
        self.doubleSpinBoxMarkerOffset.setObjectName(u"doubleSpinBoxMarkerOffset")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.doubleSpinBoxMarkerOffset)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_9)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.regButton = QPushButton(self.widget)
        self.regButton.setObjectName(u"regButton")

        self.gridLayout_2.addWidget(self.regButton, 0, 0, 1, 1)

        self.resetButton = QPushButton(self.widget)
        self.resetButton.setObjectName(u"resetButton")

        self.gridLayout_2.addWidget(self.resetButton, 0, 1, 1, 1)

        self.acceptButton = QPushButton(self.widget)
        self.acceptButton.setObjectName(u"acceptButton")

        self.gridLayout_2.addWidget(self.acceptButton, 1, 1, 1, 1)

        self.abortButton = QPushButton(self.widget)
        self.abortButton.setObjectName(u"abortButton")

        self.gridLayout_2.addWidget(self.abortButton, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout_3 = QFormLayout(self.groupBox)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.lineEditTransformation = QLineEdit(self.groupBox)
        self.lineEditTransformation.setObjectName(u"lineEditTransformation")
        self.lineEditTransformation.setReadOnly(True)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEditTransformation)

        self.lineEditRMSE = QLineEdit(self.groupBox)
        self.lineEditRMSE.setObjectName(u"lineEditRMSE")
        self.lineEditRMSE.setReadOnly(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEditRMSE)


        self.verticalLayout.addWidget(self.groupBox)

        self.screenshotgroup = QGroupBox(self.widget)
        self.screenshotgroup.setObjectName(u"screenshotgroup")
        self.screenshotgroup.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout = QFormLayout(self.screenshotgroup)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.pixelsXLabel = QLabel(self.screenshotgroup)
        self.pixelsXLabel.setObjectName(u"pixelsXLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pixelsXLabel.sizePolicy().hasHeightForWidth())
        self.pixelsXLabel.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.pixelsXLabel)

        self.screenshotPixelXLineEdit = QLineEdit(self.screenshotgroup)
        self.screenshotPixelXLineEdit.setObjectName(u"screenshotPixelXLineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.screenshotPixelXLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotPixelXLineEdit.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.screenshotPixelXLineEdit)

        self.pixelsYLabel = QLabel(self.screenshotgroup)
        self.pixelsYLabel.setObjectName(u"pixelsYLabel")
        sizePolicy2.setHeightForWidth(self.pixelsYLabel.sizePolicy().hasHeightForWidth())
        self.pixelsYLabel.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.pixelsYLabel)

        self.screenshotPixelYLineEdit = QLineEdit(self.screenshotgroup)
        self.screenshotPixelYLineEdit.setObjectName(u"screenshotPixelYLineEdit")
        sizePolicy3.setHeightForWidth(self.screenshotPixelYLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotPixelYLineEdit.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.screenshotPixelYLineEdit)

        self.screenshotFilenameLabel = QLabel(self.screenshotgroup)
        self.screenshotFilenameLabel.setObjectName(u"screenshotFilenameLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.screenshotFilenameLabel)

        self.screenshotFilenameLineEdit = QLineEdit(self.screenshotgroup)
        self.screenshotFilenameLineEdit.setObjectName(u"screenshotFilenameLineEdit")
        sizePolicy3.setHeightForWidth(self.screenshotFilenameLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotFilenameLineEdit.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.screenshotFilenameLineEdit)

        self.screenshotSaveButton = QPushButton(self.screenshotgroup)
        self.screenshotSaveButton.setObjectName(u"screenshotSaveButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.screenshotSaveButton.sizePolicy().hasHeightForWidth())
        self.screenshotSaveButton.setSizePolicy(sizePolicy4)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.screenshotSaveButton)


        self.verticalLayout.addWidget(self.screenshotgroup)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.MayaviScene = MayaviSceneWidget(self.widgetMain)
        self.MayaviScene.setObjectName(u"MayaviScene")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.MayaviScene.sizePolicy().hasHeightForWidth())
        self.MayaviScene.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.MayaviScene, 0, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.widgetMain)

        QWidget.setTabOrder(self.tableWidget, self.comboBoxLC)
        QWidget.setTabOrder(self.comboBoxLC, self.comboBoxMC)
        QWidget.setTabOrder(self.comboBoxMC, self.comboBoxLM)
        QWidget.setTabOrder(self.comboBoxLM, self.comboBoxMM)
        QWidget.setTabOrder(self.comboBoxMM, self.comboBoxTT)
        QWidget.setTabOrder(self.comboBoxTT, self.comboBoxKC)
        QWidget.setTabOrder(self.comboBoxKC, self.doubleSpinBoxMarkerOffset)
        QWidget.setTabOrder(self.doubleSpinBoxMarkerOffset, self.regButton)
        QWidget.setTabOrder(self.regButton, self.resetButton)
        QWidget.setTabOrder(self.resetButton, self.abortButton)
        QWidget.setTabOrder(self.abortButton, self.acceptButton)
        QWidget.setTabOrder(self.acceptButton, self.lineEditRMSE)
        QWidget.setTabOrder(self.lineEditRMSE, self.lineEditTransformation)
        QWidget.setTabOrder(self.lineEditTransformation, self.screenshotPixelXLineEdit)
        QWidget.setTabOrder(self.screenshotPixelXLineEdit, self.screenshotPixelYLineEdit)
        QWidget.setTabOrder(self.screenshotPixelYLineEdit, self.screenshotFilenameLineEdit)
        QWidget.setTabOrder(self.screenshotFilenameLineEdit, self.screenshotSaveButton)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Tibia Fibula PCA Landmark Registration", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Visible", None));
        self.label.setText(QCoreApplication.translate("Dialog", u"Lat. Maleolus:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Med. Maleolus:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Tib. Tuberosity:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Lat. Epicondyle:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Med. Epicondyle:", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Knee Centre:", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Marker Offset:", None))
        self.regButton.setText(QCoreApplication.translate("Dialog", u"Register", None))
        self.resetButton.setText(QCoreApplication.translate("Dialog", u"Reset", None))
        self.acceptButton.setText(QCoreApplication.translate("Dialog", u"Accept", None))
        self.abortButton.setText(QCoreApplication.translate("Dialog", u"Abort", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Registration Results", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"RMSE:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Transformation:", None))
        self.screenshotgroup.setTitle(QCoreApplication.translate("Dialog", u"Screenshot", None))
        self.pixelsXLabel.setText(QCoreApplication.translate("Dialog", u"Pixels X:", None))
        self.screenshotPixelXLineEdit.setText(QCoreApplication.translate("Dialog", u"800", None))
        self.pixelsYLabel.setText(QCoreApplication.translate("Dialog", u"Pixels Y:", None))
        self.screenshotPixelYLineEdit.setText(QCoreApplication.translate("Dialog", u"600", None))
        self.screenshotFilenameLabel.setText(QCoreApplication.translate("Dialog", u"Filename:", None))
        self.screenshotFilenameLineEdit.setText(QCoreApplication.translate("Dialog", u"screenshot.png", None))
        self.screenshotSaveButton.setText(QCoreApplication.translate("Dialog", u"Save Screenshot", None))
    # retranslateUi

