import os.path as path
import time
import math
from TurningPerf import *
from speedPerf import *
from stopPerf import *
from ContinousPerf import *
from PedstranianPerf import *


def analyse(log_path):
    # Define road stripes for first square.
    line1_1 = [[-81, -70], [-5, 7]]
    line1_2 = [[-94, -82], [-20, -7]]
    # Define road stripes for second square.
    line2_1 = [[-94, -82], [-135, -120]]
    line2_2 = [[-77, -60], [-150, -138]]
    # Define road stripes for third square.
    line3_1 = [[55, 70], [-148, -136]]
    line3_2 = [[72, 84], [-134, -120]]
    # Define road stripes for four square.
    line4_1 = [[71.5, 83.5], [-25, -10]]
    line4_2 = [[50, 67], [-8, 4]]
    # Define road stripes for fifth square.
    line5_1 = [[-13, 3], [-9.5, 2.5]]
    line5_2 = [[-29, -17], [-28, -14]]
    # Define the speed sign place
    Speed_sign1 = [[-30, -15], [-5, 7]]
    Speed_sign2 = [[-82, -65], [-150, -138]]
    Speed_sign3 = [[40, 56], [-8, 4]]
    # Define the pedstranian sign place
    Ped_sign1 = [[-94, -82], [-80, -70]]
    Ped_sign2 = [[5, 15], [-150, -138]]
    Ped_sign3 = [[72, 84], [-105, -95]]
    Ped_sign4 = [[15, 25], [-8, 4]]
    # Define the stop sign place and the boundary flags for performance testing.
    Stop_sign = [[-29, -17], [-70, -55]]
    # Define road lane boundaries to compute deviation from the road.
    Deviation1 = [[-81, 0], [-5, 7]]
    Deviation2 = [[-94, -82], [-137, -6]]
    Deviation3 = [[71, -81], [-150, -138]]
    Deviation4 = [[72, 84], [-137, -7]]
    Deviation5 = [[-16, 71], [-8, 4]]
    Deviation6 = [[-29, -17], [-400, -9]]

    ContinousPerf = []
    LastContPerf = 1
    CrossedSpeedSign1 = False
    CrossedSpeedSign2 = False
    CrossedSpeedSign3 = False
    CrossedPedSign1 = False
    CrossedPedSign2 = False
    CrossedPedSign3 = False
    CrossedPedSign4 = False
    CrossedStopSign = False
    crossedTurn1 = False
    crossedTurn2 = False
    crossedTurn3 = False
    crossedTurn4 = False
    crossedTurn5 = False

    TurnPerf = []
    SpeedPerf1 = 1
    SpeedPerf2 = 1
    SpeedPerf3 = 1
    PedPerf1 = 1
    PedPerf2 = 1
    PedPerf3 = 1
    PedPerf4 = 1
    StopPerf = 1
    TotalDevPerf = 0
    print("RECORDING STARTED!")
    with open(log_path, 'r') as f:
        # loop on the recorded file line by line and split the line.
        cnt = 0
        for l in f.readlines():
            line = l.split()
			# Check whether the line is empty.
            if(len(line) == 0 or cnt<=10):
                cnt+=1
                continue
			# Data extraction.
            time, x, y, z, Q_W,	Q_X, Q_Y, Q_Z, Throttle, Steering, Brake, Gear, Handbrake, RPM, Speed  = float(line[0]), float(line[1]), float(line[2]),float(line[3]),float(line[4]),float(line[5]),float(line[6]),float(line[7]),float(line[8]),float(line[9]),float(line[10]),float(line[11]),float(line[12]),float(line[13]),float(line[14])

            cnt+=1
			#------------------------------- turning performance part-------------------------------------
            TurnPerfTemp,crossedTurn1 = VerticalTurnLRFromLRLane(line1_1, line1_2, crossedTurn1, x, y)
            if(TurnPerfTemp!=0):
                TurnPerf.append(TurnPerfTemp)
            
            TurnPerfTemp2,crossedTurn2 = HorizontalTurnLRFromLRLane(line2_1, line2_2, crossedTurn2, x, y)
            if(TurnPerfTemp2!=0):
                TurnPerf.append(TurnPerfTemp2)

            TurnPerfTemp3,crossedTurn3 = VerticalTurnLRFromRLLane(line3_1, line3_2, crossedTurn3, x, y)
            if(TurnPerfTemp3!=0):
                TurnPerf.append(TurnPerfTemp3)

            TurnPerfTemp4,crossedTurn4 = HorizontalTurnLRFromRLLane(line4_1, line4_2, crossedTurn4, x, y)
            if(TurnPerfTemp4!=0):
                TurnPerf.append(TurnPerfTemp4)

            TurnPerfTemp5,crossedTurn5 = VerticalTurnLRFromLRLane(line5_1, line5_2, crossedTurn5, x, y)
            if(TurnPerfTemp5!=0):
                TurnPerf.append(TurnPerfTemp5)        

            # ------------------------------- Speed limit performance part-------------------------------------
            SpeedPerf1,CrossedSpeedSign1 = SpeedSign(Speed_sign1, CrossedSpeedSign1, x, y, Speed, SpeedPerf1, 20)
            SpeedPerf2,CrossedSpeedSign2 = SpeedSign(Speed_sign2, CrossedSpeedSign2, x, y, Speed, SpeedPerf2, 30)
            SpeedPerf3,CrossedSpeedSign3 = SpeedSign(Speed_sign3, CrossedSpeedSign3, x, y, Speed, SpeedPerf3, 20)
            if(CrossedSpeedSign2):
                CrossedSpeedSign1 = False
            if(CrossedSpeedSign3):
                CrossedSpeedSign2 = False    
			#------------------------------- Pedstranian sign performance part-------------------------------------
            PedPerf1,CrossedPedSign1 = PedstranianSignLeft(Ped_sign1, CrossedPedSign1, x, y, Speed, PedPerf1)
            PedPerf2,CrossedPedSign2 = PedstranianSignUp(Ped_sign2, CrossedPedSign2, x, y, Speed, PedPerf2)
            PedPerf3,CrossedPedSign3 = PedstranianSignRight(Ped_sign3, CrossedPedSign3, x, y, Speed, PedPerf3)
            PedPerf4,CrossedPedSign4 = PedstranianSignDown(Ped_sign4, CrossedPedSign4, x, y, Speed, PedPerf4)
            #------------------------------- Stop sign performance part-------------------------------------
            StopPerf,CrossedStopSign = StopSignLeft(Stop_sign, CrossedStopSign, x, y, Speed, StopPerf)

			#------------------------------- continous deviation performance part-------------------------------------
            if(crossedTurn1 or crossedTurn2 or crossedTurn3 or crossedTurn4 or crossedTurn5):
                ContinousPerf.append([time,LastContPerf])
                TotalDevPerf+=LastContPerf
                continue
            LastContPerfTemp1 = MovVerticalRightLane(Deviation1,x,y)
            LastContPerfTemp2 = MovHorizontalDownLane(Deviation2,x,y)
            LastContPerfTemp3 = MovVerticalLeftLane(Deviation3,x,y)
            LastContPerfTemp4 = MovHorizontalupLane(Deviation4,x,y)
            LastContPerfTemp5 = MovVerticalRightLane(Deviation5,x,y)
            LastContPerfTemp6 = MovHorizontalDownLane(Deviation6,x,y)
            if(LastContPerfTemp1!=0):
                LastContPerf = LastContPerfTemp1
                ContinousPerf.append([time,LastContPerf])
            if(LastContPerfTemp2!=0):
                LastContPerf = LastContPerfTemp2
                ContinousPerf.append([time,LastContPerf])
            if(LastContPerfTemp3!=0):
                LastContPerf = LastContPerfTemp3
                ContinousPerf.append([time,LastContPerf]) 
            if(LastContPerfTemp4!=0):
                LastContPerf = LastContPerfTemp4
                ContinousPerf.append([time,LastContPerf]) 
            if(LastContPerfTemp5!=0):
                LastContPerf = LastContPerfTemp5
                ContinousPerf.append([time,LastContPerf])
            if(LastContPerfTemp6!=0):
                LastContPerf = LastContPerfTemp6
                ContinousPerf.append([time,LastContPerf])           
            TotalDevPerf+=LastContPerf
#=============================================result================================================
        DevPerf = math.ceil(TotalDevPerf/(cnt-10))
        TurnPerfTotal = math.ceil(sum(TurnPerf))
        SpeedPerfTotal = math.ceil((SpeedPerf1+SpeedPerf2+SpeedPerf3))
        PedPerfTotal = math.ceil((PedPerf1+PedPerf2+PedPerf3+PedPerf4))
        print("performance turn: " + str(TurnPerf))
        print("performance speed1: " + str(SpeedPerf1))
        print("performance speed2: " + str(SpeedPerf2))
        print("performance speed3: " + str(SpeedPerf3))
        print("performance ped1: " + str(PedPerf1))
        print("performance ped2: " + str(PedPerf2))
        print("performance ped3: " + str(PedPerf3))
        print("performance ped4: " + str(PedPerf4))
        print("performance stop: " + str(StopPerf)) 
        print("performance deviation: " + str(DevPerf))
        return ( DevPerf + SpeedPerfTotal + PedPerfTotal + StopPerf + TurnPerfTotal ) /14, ContinousPerf

