# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oldtimer.ui'
#
# Created: Thu Sep 29 23:36:33 2011
#      by: pyside-uic 0.2.8 running on PySide 1.0.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(504, 570)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonQuit = QtGui.QPushButton(self.centralwidget)
        self.buttonQuit.setGeometry(QtCore.QRect(401, 490, 80, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonQuit.sizePolicy().hasHeightForWidth())
        self.buttonQuit.setSizePolicy(sizePolicy)
        self.buttonQuit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonQuit.setFlat(False)
        self.buttonQuit.setObjectName("buttonQuit")
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 461, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayoutPlotSettings = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayoutPlotSettings.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayoutPlotSettings.setContentsMargins(-1, -1, -1, 0)
        self.gridLayoutPlotSettings.setHorizontalSpacing(6)
        self.gridLayoutPlotSettings.setObjectName("gridLayoutPlotSettings")
        self.labelYaxis = QtGui.QLabel(self.layoutWidget)
        self.labelYaxis.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelYaxis.setObjectName("labelYaxis")
        self.gridLayoutPlotSettings.addWidget(self.labelYaxis, 1, 0, 1, 1)
        self.buttonPlot = QtGui.QPushButton(self.layoutWidget)
        self.buttonPlot.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonPlot.sizePolicy().hasHeightForWidth())
        self.buttonPlot.setSizePolicy(sizePolicy)
        self.buttonPlot.setObjectName("buttonPlot")
        self.gridLayoutPlotSettings.addWidget(self.buttonPlot, 2, 1, 1, 1)
        self.comboYAxis = QtGui.QComboBox(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboYAxis.sizePolicy().hasHeightForWidth())
        self.comboYAxis.setSizePolicy(sizePolicy)
        self.comboYAxis.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.comboYAxis.setObjectName("comboYAxis")
        self.gridLayoutPlotSettings.addWidget(self.comboYAxis, 1, 2, 1, 1)
        self.comboYLog = QtGui.QComboBox(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboYLog.sizePolicy().hasHeightForWidth())
        self.comboYLog.setSizePolicy(sizePolicy)
        self.comboYLog.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.comboYLog.setObjectName("comboYLog")
        self.gridLayoutPlotSettings.addWidget(self.comboYLog, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayoutPlotSettings.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayoutPlotSettings.addWidget(self.label_2, 0, 2, 1, 1)
        self.checkBoxStep = QtGui.QCheckBox(self.layoutWidget)
        self.checkBoxStep.setChecked(True)
        self.checkBoxStep.setObjectName("checkBoxStep")
        self.gridLayoutPlotSettings.addWidget(self.checkBoxStep, 2, 2, 1, 1)
        self.labelResolution = QtGui.QLabel(self.layoutWidget)
        self.labelResolution.setObjectName("labelResolution")
        self.gridLayoutPlotSettings.addWidget(self.labelResolution, 0, 3, 1, 1)
        self.comboResolution = QtGui.QComboBox(self.layoutWidget)
        self.comboResolution.setObjectName("comboResolution")
        self.gridLayoutPlotSettings.addWidget(self.comboResolution, 1, 3, 1, 1)
        self.gridLayoutPlotSettings.setColumnStretch(2, 1)
        self.gridLayoutPlotSettings.setColumnStretch(3, 1)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 160, 461, 317))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelText1 = QtGui.QLabel(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelText1.sizePolicy().hasHeightForWidth())
        self.labelText1.setSizePolicy(sizePolicy)
        self.labelText1.setText("")
        self.labelText1.setObjectName("labelText1")
        self.gridLayout_2.addWidget(self.labelText1, 1, 0, 1, 1)
        self.labelText2 = QtGui.QLabel(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelText2.sizePolicy().hasHeightForWidth())
        self.labelText2.setSizePolicy(sizePolicy)
        self.labelText2.setText("")
        self.labelText2.setObjectName("labelText2")
        self.gridLayout_2.addWidget(self.labelText2, 1, 1, 1, 1)
        self.textEdit1 = QtGui.QTextEdit(self.layoutWidget1)
        self.textEdit1.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.textEdit1.setReadOnly(True)
        self.textEdit1.setObjectName("textEdit1")
        self.gridLayout_2.addWidget(self.textEdit1, 2, 0, 1, 1)
        self.textEdit2 = QtGui.QTextEdit(self.layoutWidget1)
        self.textEdit2.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.textEdit2.setReadOnly(True)
        self.textEdit2.setObjectName("textEdit2")
        self.gridLayout_2.addWidget(self.textEdit2, 2, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 504, 25))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.actionE_xit = QtGui.QAction(MainWindow)
        self.actionE_xit.setObjectName("actionE_xit")
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.actionE_xit)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionE_xit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QObject.connect(self.buttonQuit, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Oldtimer", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonQuit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.labelYaxis.setText(QtGui.QApplication.translate("MainWindow", "Y Axis:", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonPlot.setText(QtGui.QApplication.translate("MainWindow", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Log", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Axis", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxStep.setText(QtGui.QApplication.translate("MainWindow", "Step", None, QtGui.QApplication.UnicodeUTF8))
        self.labelResolution.setText(QtGui.QApplication.translate("MainWindow", "Resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionE_xit.setText(QtGui.QApplication.translate("MainWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))

