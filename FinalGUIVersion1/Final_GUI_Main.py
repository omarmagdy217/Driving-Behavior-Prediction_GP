# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Final_GUI_Window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 669)
        MainWindow.setMinimumSize(QtCore.QSize(700, 669))
        MainWindow.setMaximumSize(QtCore.QSize(700, 753))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(700, 700))
        self.centralwidget.setMaximumSize(QtCore.QSize(700, 700))
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(22, 407, 661, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 20, 692, 624))
        self.widget.setObjectName("widget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.The_GUI_LABLE = QtWidgets.QLabel(self.widget)
        self.The_GUI_LABLE.setMinimumSize(QtCore.QSize(511, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.The_GUI_LABLE.setFont(font)
        self.The_GUI_LABLE.setStyleSheet("color: rgb(170, 0, 0);")
        self.The_GUI_LABLE.setAlignment(QtCore.Qt.AlignCenter)
        self.The_GUI_LABLE.setObjectName("The_GUI_LABLE")
        self.gridLayout_3.addWidget(self.The_GUI_LABLE, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setObjectName("gridLayout")
        self.GUI_Steps_to_Start = QtWidgets.QLabel(self.widget)
        self.GUI_Steps_to_Start.setMinimumSize(QtCore.QSize(131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.GUI_Steps_to_Start.setFont(font)
        self.GUI_Steps_to_Start.setStyleSheet("color: rgb(255, 0, 127);")
        self.GUI_Steps_to_Start.setLineWidth(0)
        self.GUI_Steps_to_Start.setObjectName("GUI_Steps_to_Start")
        self.gridLayout.addWidget(self.GUI_Steps_to_Start, 0, 0, 1, 1)
        self.JustWaitNow = QtWidgets.QLabel(self.widget)
        self.JustWaitNow.setMinimumSize(QtCore.QSize(131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.JustWaitNow.setFont(font)
        self.JustWaitNow.setStyleSheet("color: rgb(255, 6, 6);")
        self.JustWaitNow.setLineWidth(0)
        self.JustWaitNow.setObjectName("JustWaitNow")
        self.gridLayout.addWidget(self.JustWaitNow, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.GUI_CHECK_1 = QtWidgets.QCheckBox(self.widget)
        self.GUI_CHECK_1.setMinimumSize(QtCore.QSize(181, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GUI_CHECK_1.setFont(font)
        self.GUI_CHECK_1.setObjectName("GUI_CHECK_1")
        self.verticalLayout.addWidget(self.GUI_CHECK_1)
        self.GUI_CHECK_2 = QtWidgets.QCheckBox(self.widget)
        self.GUI_CHECK_2.setMinimumSize(QtCore.QSize(251, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GUI_CHECK_2.setFont(font)
        self.GUI_CHECK_2.setObjectName("GUI_CHECK_2")
        self.verticalLayout.addWidget(self.GUI_CHECK_2)
        self.GUI_CHECK_3 = QtWidgets.QCheckBox(self.widget)
        self.GUI_CHECK_3.setMinimumSize(QtCore.QSize(251, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GUI_CHECK_3.setFont(font)
        self.GUI_CHECK_3.setObjectName("GUI_CHECK_3")
        self.verticalLayout.addWidget(self.GUI_CHECK_3)
        self.StartRecordingBtn = QtWidgets.QPushButton(self.widget)
        self.StartRecordingBtn.setMinimumSize(QtCore.QSize(306, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.StartRecordingBtn.setFont(font)
        self.StartRecordingBtn.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"color: rgb(0, 255, 17);")
        self.StartRecordingBtn.setObjectName("StartRecordingBtn")
        self.verticalLayout.addWidget(self.StartRecordingBtn)
        self.RecordingFinished = QtWidgets.QLabel(self.widget)
        self.RecordingFinished.setEnabled(False)
        self.RecordingFinished.setMinimumSize(QtCore.QSize(131, 51))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.RecordingFinished.setFont(font)
        self.RecordingFinished.setStyleSheet("color: rgb(255, 0, 127);")
        self.RecordingFinished.setLineWidth(0)
        self.RecordingFinished.setAlignment(QtCore.Qt.AlignCenter)
        self.RecordingFinished.setObjectName("RecordingFinished")
        self.verticalLayout.addWidget(self.RecordingFinished)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.NotImportantLable = QtWidgets.QLabel(self.widget)
        self.NotImportantLable.setEnabled(False)
        self.NotImportantLable.setMinimumSize(QtCore.QSize(251, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.NotImportantLable.setFont(font)
        self.NotImportantLable.setStyleSheet("color: rgb(0, 170, 255);")
        self.NotImportantLable.setLineWidth(0)
        self.NotImportantLable.setAlignment(QtCore.Qt.AlignCenter)
        self.NotImportantLable.setObjectName("NotImportantLable")
        self.verticalLayout_2.addWidget(self.NotImportantLable)
        self.MentalStatePart = QtWidgets.QLabel(self.widget)
        self.MentalStatePart.setEnabled(False)
        self.MentalStatePart.setMinimumSize(QtCore.QSize(251, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.MentalStatePart.setFont(font)
        self.MentalStatePart.setStyleSheet("color: rgb(0, 170, 0);")
        self.MentalStatePart.setLineWidth(0)
        self.MentalStatePart.setAlignment(QtCore.Qt.AlignCenter)
        self.MentalStatePart.setObjectName("MentalStatePart")
        self.verticalLayout_2.addWidget(self.MentalStatePart)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_9.setHorizontalSpacing(20)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.EndDrivingBTN = QtWidgets.QPushButton(self.widget)
        self.EndDrivingBTN.setMinimumSize(QtCore.QSize(459, 40))
        self.EndDrivingBTN.setMaximumSize(QtCore.QSize(459, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.EndDrivingBTN.setFont(font)
        self.EndDrivingBTN.setStyleSheet("background-color: rgb(170, 85, 127);\n"
"color: rgb(194, 8, 8);")
        self.EndDrivingBTN.setObjectName("EndDrivingBTN")
        self.horizontalLayout.addWidget(self.EndDrivingBTN)
        spacerItem1 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_9.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setContentsMargins(5, 15, 0, -1)
        self.gridLayout_8.setHorizontalSpacing(11)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.graphicsView = PlotWidget(self.widget)
        self.graphicsView.setMinimumSize(QtCore.QSize(461, 271))
        self.graphicsView.setMaximumSize(QtCore.QSize(461, 271))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_8.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.g1 = QtWidgets.QLabel(self.widget)
        self.g1.setMinimumSize(QtCore.QSize(21, 21))
        self.g1.setMaximumSize(QtCore.QSize(21, 21))
        self.g1.setStyleSheet("background-color: rgb(85, 255, 23);")
        self.g1.setText("")
        self.g1.setObjectName("g1")
        self.gridLayout_7.addWidget(self.g1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 0, 1, 1, 1)
        self.g2 = QtWidgets.QLabel(self.widget)
        self.g2.setMinimumSize(QtCore.QSize(161, 21))
        self.g2.setMaximumSize(QtCore.QSize(161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.g2.setFont(font)
        self.g2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.g2.setAlignment(QtCore.Qt.AlignCenter)
        self.g2.setObjectName("g2")
        self.gridLayout_7.addWidget(self.g2, 0, 2, 1, 1)
        self.g3 = QtWidgets.QLabel(self.widget)
        self.g3.setMinimumSize(QtCore.QSize(21, 21))
        self.g3.setMaximumSize(QtCore.QSize(21, 21))
        self.g3.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.g3.setText("")
        self.g3.setObjectName("g3")
        self.gridLayout_7.addWidget(self.g3, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem3, 1, 1, 1, 1)
        self.g4 = QtWidgets.QLabel(self.widget)
        self.g4.setMinimumSize(QtCore.QSize(161, 21))
        self.g4.setMaximumSize(QtCore.QSize(161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.g4.setFont(font)
        self.g4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.g4.setAlignment(QtCore.Qt.AlignCenter)
        self.g4.setObjectName("g4")
        self.gridLayout_7.addWidget(self.g4, 1, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_7)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.l1 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.l1.setFont(font)
        self.l1.setStyleSheet("color: rgb(170, 0, 127);")
        self.l1.setMidLineWidth(0)
        self.l1.setTextFormat(QtCore.Qt.AutoText)
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        self.l1.setObjectName("l1")
        self.gridLayout_5.addWidget(self.l1, 0, 0, 1, 1)
        self.l2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.l2.setFont(font)
        self.l2.setStyleSheet("color: rgb(170, 0, 127);")
        self.l2.setMidLineWidth(0)
        self.l2.setTextFormat(QtCore.Qt.AutoText)
        self.l2.setAlignment(QtCore.Qt.AlignCenter)
        self.l2.setObjectName("l2")
        self.gridLayout_5.addWidget(self.l2, 1, 0, 1, 1)
        self.l3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.l3.setFont(font)
        self.l3.setStyleSheet("color: rgb(170, 0, 127);")
        self.l3.setMidLineWidth(0)
        self.l3.setTextFormat(QtCore.Qt.AutoText)
        self.l3.setAlignment(QtCore.Qt.AlignCenter)
        self.l3.setObjectName("l3")
        self.gridLayout_5.addWidget(self.l3, 2, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.R1 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.R1.setFont(font)
        self.R1.setStyleSheet("color: rgb(0, 85, 0);")
        self.R1.setAlignment(QtCore.Qt.AlignCenter)
        self.R1.setObjectName("R1")
        self.gridLayout_4.addWidget(self.R1, 0, 0, 1, 1)
        self.R2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.R2.setFont(font)
        self.R2.setStyleSheet("color: rgb(0, 85, 0);")
        self.R2.setAlignment(QtCore.Qt.AlignCenter)
        self.R2.setObjectName("R2")
        self.gridLayout_4.addWidget(self.R2, 1, 0, 1, 1)
        self.R3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.R3.setFont(font)
        self.R3.setStyleSheet("color: rgb(0, 85, 0);")
        self.R3.setAlignment(QtCore.Qt.AlignCenter)
        self.R3.setObjectName("R3")
        self.gridLayout_4.addWidget(self.R3, 2, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 1, 1, 1, 1)
        self.l0 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(28)
        self.l0.setFont(font)
        self.l0.setStyleSheet("color: rgb(170, 170, 0);")
        self.l0.setAlignment(QtCore.Qt.AlignCenter)
        self.l0.setObjectName("l0")
        self.gridLayout_6.addWidget(self.l0, 0, 0, 1, 2)
        self.verticalLayout_3.addLayout(self.gridLayout_6)
        self.gridLayout_8.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 1, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.The_GUI_LABLE.setText(_translate("MainWindow", "Preformance and Mental State Pridection Using EEG"))
        self.GUI_Steps_to_Start.setText(_translate("MainWindow", "Steps To Start:"))
        self.JustWaitNow.setText(_translate("MainWindow", "Just Wait Now"))
        self.GUI_CHECK_1.setText(_translate("MainWindow", "Make Sure Head Set is ON"))
        self.GUI_CHECK_2.setText(_translate("MainWindow", "Make Sure You Wear the Head Set well"))
        self.GUI_CHECK_3.setText(_translate("MainWindow", "You Know that you need to record for 30 sec now"))
        self.StartRecordingBtn.setText(_translate("MainWindow", "Start Recording Now"))
        self.RecordingFinished.setText(_translate("MainWindow", "We Have Recorded Succesfully \n"
"You Can Start Driving Now"))
        self.NotImportantLable.setText(_translate("MainWindow", "Your Current Mental\n"
" State:"))
        self.MentalStatePart.setText(_translate("MainWindow", "Foucused"))
        self.EndDrivingBTN.setText(_translate("MainWindow", "Finish Driving / Show Driving Analysis Now"))
        self.g2.setText(_translate("MainWindow", "Model Prediction"))
        self.g4.setText(_translate("MainWindow", "Actual Prediction"))
        self.l1.setText(_translate("MainWindow", "Focused"))
        self.l2.setText(_translate("MainWindow", "De-Focused"))
        self.l3.setText(_translate("MainWindow", "Drowsy"))
        self.R1.setText(_translate("MainWindow", "30%"))
        self.R2.setText(_translate("MainWindow", "30%"))
        self.R3.setText(_translate("MainWindow", "30%"))
        self.l0.setText(_translate("MainWindow", "RESULTS"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
