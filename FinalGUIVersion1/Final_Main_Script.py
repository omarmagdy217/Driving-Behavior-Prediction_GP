from Final_GUI_Main import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Final_Head_Set_Handler import *
from Final_Online_Mode_Classifier import *
import operator
import os
import threading
import time
import subprocess
from Final_performan_escripts.main import compute
from Final_Rank_prediction.ranks_scripts import *


predicted_preformance=[30,40,90,10,40,30]
ACtual_preformance=[0,0,0,0,0,10]
Mind_State=[]
Stadges=[1,2,3,4,5,6]



class MainWindow(QMainWindow, Ui_MainWindow):
    are_we_okay=True
    state=0
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.EndDrivingBTN.clicked.connect(self.End_Driving)
        self.StartRecordingBtn.clicked.connect(self.Start_Recording)
        self.JustWaitNow.hide()
        self.MentalStatePart.hide()
        self.RecordingFinished.hide()
        self.hide_resluts()
        self.EndDrivingBTN.setEnabled(False)
        self.show()

    def hide_resluts(self):
        self.l0.hide()
        self.l1.hide()
        self.l2.hide()
        self.l3.hide()
        self.R1.hide()
        self.R2.hide()
        self.R3.hide()
        self.g1.hide()
        self.g2.hide()
        self.g3.hide()
        self.g4.hide()

    def show_resluts(self):
        self.l0.show()
        self.l1.show()
        self.l2.show()
        self.l3.show()
        self.R1.show()
        self.R2.show()
        self.R3.show()

    def draw_graph(self,x):
        global ACtual_preformance
        global predicted_preformance
        if(x==1):
            self.graphicsView.setLabels(title='Preformance Results', bottom= ' Stadges' ,  left='Performance')
            self.graphicsView.plot( Stadges , predicted_preformance , pen=(1, 3) )
            self.g1.show()
            self.g2.show()
        if (x == 2):
            self.graphicsView.plot( Stadges , ACtual_preformance, pen=(2, 3))
            self.g3.show()
            self.g4.show()

    def show_precent_of_each_state(self):
        total=len(Mind_State)
        n1=0
        n2=0
        n3=0
        for item in Mind_State:
            if(item=="Focused"):
                n1 = n1 + 1
            elif (item == "De-Focused"):
                n2 = n2 + 1
            elif (item == "Drowsy"):
                n3 = n3 + 1
        n1 = n1/ total
        n2 = n2/ total
        n3 = n3 / total
        n1 = n1 * 100
        n2 = n2 * 100
        n3 = n3 * 100
        self.R1.setText("")
        self.R2.setText("")
        self.R3.setText("")
        self.R1.setText(str(n1)+"%")
        self.R2.setText(str(n2)+"%")
        self.R3.setText(str(n3)+"%")

    def End_Driving(self):
        r = refresher()
        r.change()
        self.show_resluts()
        self.draw_graph(2)
        self.show_precent_of_each_state()
        self.are_we_okay=False
        self.RecordingFinished.hide()
        arr = compute()
        print(arr)
        self.just_copy(arr)

    def just_copy(self,arr):
        global ACtual_preformance
        global predicted_preformance
        print("===========================================")
        print(ACtual_preformance)
        print(arr)
        ACtual_preformance[0] = arr[0]
        ACtual_preformance[1] = arr[1]
        ACtual_preformance[2] = arr[2]
        ACtual_preformance[3] = arr[3]
        ACtual_preformance[4] = arr[4]
        ACtual_preformance[5] = arr[5]
        print(ACtual_preformance)
        print(arr)
        print("===========================================")

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
        Thread4 = threading.Thread(target=self.Use_ML_Model_to_predict_preformance)
        Thread4.start()

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
            self.state=s
            EmbeddedThread = threading.Thread(target=self.Send_to_embedded)
            EmbeddedThread.start()

    def just_copy(self,arr):
        global ACtual_preformance
        global predicted_preformance
        print("===========================================")
        print(predicted_preformance)
        print(arr)
        predicted_preformance[0] = arr[0]
        predicted_preformance[1] = arr[1]
        predicted_preformance[2] = arr[2]
        predicted_preformance[3] = arr[3]
        predicted_preformance[4] = arr[4]
        predicted_preformance[5] = arr[5]
        print(predicted_preformance)
        print(arr)
        print("===========================================")

    def Use_ML_Model_to_predict_preformance(self):
        arr = pass_values_to_omar()
        self.draw_graph(1)

    def Send_to_embedded(self):
        n = 0
        if(self.state=="Focused"):
            n=1
        elif (self.state == "De-Focused"):
            n = 2
        elif (self.state == "Drowsy"):
            n = 3
        f = open("Embedded_Data_to_UART.txt", 'w')
        f.write(str(n))
        f.close()

if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("MainWindow")

    window = MainWindow()
    app.exec_()