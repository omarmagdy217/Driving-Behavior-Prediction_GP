import os.path as path
import time
import math
from TurningPerf import *
from speedPerf import *
from stopPerf import *
from ContinousPerf import *


def analyse(data):
    # Define road stripes for first square.
    line1_1 = [[566.5, 578.5], [-302, -282]]
    line1_2 = [[538, 555], [-278, -266]]
    # Define the speed sign place
    Speed_sign = [[360, 380], [-278, -266]]
    # Define the stop sign place and the boundary flags for performance testing.
    Stop_sign = [[210, 230], [-278, -266]]
    # Define road lane boundaries to compute deviation from the road.
    Deviation1 = [[566.5, 578.5], [-1000, -279]]
    Deviation2 = [[-500, 566], [-278, -266]]


    ContinousPerf = []
    LastContPerf = 1
    CrossedSpeedSign = False
    CrossedStopSign = False
    crossedTurn1 = False
        
    TurnPerf = []
    SpeedPerf = 1
    StopPerf = 1
    TotalDevPerf = 0
    
    
    cnt = 0
    for l in data:
        
        # Data extraction.
        x, y, Speed = l[0], l[1], l[2] 

        cnt+=1
        #------------------------------- turning performance part-------------------------------------
        TurnPerfTemp,crossedTurn1 = HorizontalTurnLRFromLRLane(line1_1, line1_2, crossedTurn1, x, y)
        if(TurnPerfTemp!=0):
            TurnPerf.append(TurnPerfTemp)
        

        # ------------------------------- Speed limit performance part-------------------------------------
        SpeedPerf,CrossedSpeedSign = SpeedSign(Speed_sign, CrossedSpeedSign, x, y, Speed, SpeedPerf,20)
        

        #------------------------------- stop sign performance part-------------------------------------
        StopPerf,CrossedStopSign = StopSignDown(Stop_sign, CrossedStopSign, x, y, Speed, StopPerf)
        


        #------------------------------- continous deviation performance part-------------------------------------
        if(crossedTurn1):
            ContinousPerf.append([time,LastContPerf])
            TotalDevPerf+=LastContPerf
            continue
        LastContPerfTemp1 = MovHorizontalDownLane(Deviation1,x,y)
        LastContPerfTemp2 = MovVerticalLeftLane(Deviation2,x,y)
        if(LastContPerfTemp1!=0):
            LastContPerf = LastContPerfTemp1
            ContinousPerf.append([time,LastContPerf])
        if(LastContPerfTemp2!=0):
            LastContPerf = LastContPerfTemp2
            ContinousPerf.append([time,LastContPerf])        
        TotalDevPerf+=LastContPerf
#=============================================result================================================
    DevPerf = math.ceil(TotalDevPerf/(cnt))
    print("performance turn: " + str(sum(TurnPerf)))
    print("performance speed: " + str(SpeedPerf))
    print("performance stop: " + str(StopPerf)) 
    print("performance deviation: " + str(DevPerf))
    return (DevPerf+SpeedPerf+StopPerf+sum(TurnPerf))/4,ContinousPerf

