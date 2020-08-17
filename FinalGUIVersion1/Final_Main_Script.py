from Final_GUI_Main import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Final_Head_Set_Handler import *
from Final_Online_Mode_Classifier import *
import operator
import os
import threading
import time
import subprocess


predicted_preformance=[]
ACtual_preformance=[]
Mind_State=[]



class MainWindow(QMainWindow, Ui_MainWindow):
    are_we_okay=True
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.EndDrivingBTN.clicked.connect(self.End_Driving)
        self.StartRecordingBtn.clicked.connect(self.Start_Recording)

        self.JustWaitNow.hide()
        self.MentalStatePart.hide()
        self.RecordingFinished.hide()
        self.EndDrivingBTN.setEnabled(False)
        self.show()

    def End_Driving(self):
        r = refresher()
        r.change()
        self.are_we_okay=False
        self.RecordingFinished.hide()

    def Start_Recording(self):
        ch1 = self.GUI_CHECK_1.isChecked()
        ch2 = self.GUI_CHECK_2.isChecked()
        ch3 = self.GUI_CHECK_3.isChecked()
        if (ch1 and ch2 and ch3):
            self.StartRecordingBtn.setEnabled(False)
            self.JustWaitNow.show()
            Thread1 = threading.Thread(target=self.Start_our_main_loop)
            Thread1.start()
        else:
            print("Check on the Boxes First")

    def Start_our_main_loop(self):
        Start_initial_recording()
        self.JustWaitNow.hide()
        self.RecordingFinished.show()
        self.MentalStatePart.show()
        self.MentalStatePart.setText("")
        simulatorThread = threading.Thread(target=self.runSimulator)
        simulatorThread.start()
        Thread3 = threading.Thread(target=self.MentalState_analysis)
        Thread3.start()

    def runSimulator(self):
        #######################################################################
        #########          New Karaman Path Should be her      ################
        #######################################################################
        os.system('"' + os.getcwd() + "/WindowsNoEditor/MRT.exe" + '"')

    def MentalState_analysis(self):
        self.EndDrivingBTN.setEnabled(True)
        Thread4 = threading.Thread(target=StartFromHere)
        Thread4.start()
        r = refresher()
        while(self.are_we_okay):
            time.sleep(5)
            s = r.updatez()
            print(s)
            self.MentalStatePart.setText(s)
            Mind_State.append(s)

if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("MainWindow")

    window = MainWindow()
    app.exec_()