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
    line1_1 = [[60, 75], [-9, 3]]
    line1_2 = [[77, 89], [-20, -10]]
    # Define road stripes for second square.
    line2_1 = [[77, 89], [-365, -345]]
    line2_2 = [[91, 101], [-378, -366]]
    # Define road stripes for third square.
    line3_1 = [[180, 195], [-378, -366]]
    line3_2 = [[197, 209], [-360, -345]]
    # Define the speed sign place
    Speed_sign1 = [[0, 10], [-9, 3]]
    Speed_sign2 = [[77, 89], [-190, -175]]
    # Define the pedstranian sign place
    Ped_sign1 = [[77, 89], [-75, -60]]
    Ped_sign2 = [[77, 89], [-285, -270]]
    # Define the stop sign place and the boundary flags for performance testing.
    Stop_sign = [[197, 209], [-330, -318]]
    # Define road lane boundaries to compute deviation from the road.
    Deviation1 = [[0, 76], [-9, 3]]
    Deviation2 = [[77, 89], [-365, -10]]
    Deviation3 = [[90, 196], [-378, -366]]
    Deviation4 = [[197, 209], [-365, -100]]

    ContinousPerf = []
    LastContPerf = 1
    CrossedSpeedSign1 = False
    CrossedSpeedSign2 = False
    CrossedPedSign1 = False
    CrossedPedSign2 = False
    CrossedStopSign = False
    crossedTurn1 = False
    crossedTurn2 = False
    crossedTurn3 = False

    TurnPerf = []
    SpeedPerf1 = 1
    SpeedPerf2 = 1
    PedPerf1 = 1
    PedPerf2 = 1
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
            TurnPerfTemp,crossedTurn1 = VerticalTurnLRFromRLLane(line1_1, line1_2, crossedTurn1, x, y)
            if(TurnPerfTemp!=0):
                TurnPerf.append(TurnPerfTemp)
            
            TurnPerfTemp2,crossedTurn2 = HorizontalTurnLRFromRLLane(line2_1, line2_2, crossedTurn2, x, y)
            if(TurnPerfTemp2!=0):
                TurnPerf.append(TurnPerfTemp2)

            TurnPerfTemp3,crossedTurn3 = VerticalTurnLRFromLRLane(line3_1, line3_2, crossedTurn3, x, y)
            if(TurnPerfTemp3!=0):
                TurnPerf.append(TurnPerfTemp3)

            # ------------------------------- Speed limit performance part-------------------------------------
            SpeedPerf1,CrossedSpeedSign1 = SpeedSign(Speed_sign1, CrossedSpeedSign1, x, y, Speed, SpeedPerf1, 20)
            SpeedPerf2,CrossedSpeedSign2 = SpeedSign(Speed_sign2, CrossedSpeedSign2, x, y, Speed, SpeedPerf2, 30)
            if(CrossedSpeedSign2):
                CrossedSpeedSign1 = False
			#------------------------------- Pedstranian sign performance part-------------------------------------
            PedPerf1,CrossedPedSign1 = PedstranianSignLeft(Ped_sign1, CrossedPedSign1, x, y, Speed, PedPerf1)
            PedPerf2,CrossedPedSign2 = PedstranianSignLeft(Ped_sign2, CrossedPedSign2, x, y, Speed, PedPerf2)
            #------------------------------- Stop sign performance part-------------------------------------
            StopPerf,CrossedStopSign = StopSignRight(Stop_sign, CrossedStopSign, x, y, Speed, StopPerf)

			#------------------------------- continous deviation performance part-------------------------------------
            if(crossedTurn1 or crossedTurn2 or crossedTurn3):
                ContinousPerf.append([time,LastContPerf])
                TotalDevPerf+=LastContPerf
                continue
            LastContPerfTemp1 = MovVerticalRightLane(Deviation1,x,y)
            LastContPerfTemp2 = MovHorizontalupLane(Deviation2,x,y)
            LastContPerfTemp3 = MovVerticalRightLane(Deviation3,x,y)
            LastContPerfTemp4 = MovHorizontalDownLane(Deviation4,x,y)
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
            TotalDevPerf+=LastContPerf
#=============================================result================================================
        DevPerf = math.ceil(TotalDevPerf/(cnt-10))
        TurnPerfTotal = math.ceil(sum(TurnPerf))
        SpeedPerfTotal = math.ceil((SpeedPerf1+SpeedPerf2))
        PedPerfTotal = math.ceil((PedPerf1+PedPerf2))
        print("performance turn: " + str(TurnPerf))
        print("performance speed1: " + str(SpeedPerf1))
        print("performance speed2: " + str(SpeedPerf2))
        print("performance ped1: " + str(PedPerf1))
        print("performance ped2: " + str(PedPerf2))
        print("performance stop: " + str(StopPerf)) 
        print("performance deviation: " + str(DevPerf))
        return ( DevPerf + SpeedPerfTotal + PedPerfTotal + StopPerf + TurnPerfTotal ) /9, ContinousPerf

