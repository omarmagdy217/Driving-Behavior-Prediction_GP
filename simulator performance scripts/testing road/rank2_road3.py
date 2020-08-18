import os.path as path
import time
import math
from TurningPerf import *
from speedPerf import *
from stopPerf import *
from ContinousPerf import *
from PedstranianPerf import *


def analyse(data):
    # Define road stripes for first square.
    line1_1 = [[280, 295], [-577, -565]]
    line1_2 = [[266.5, 278.5], [-559, -545]]
    # Define road stripes for second square.
    line2_1 = [[266.5, 278.5], [-375, -355]]
    line2_2 = [[287, 307], [-353, -341]]
    # Define road stripes for third square.
    line3_1 = [[539, 559], [-353.5, -341.5]]
    line3_2 = [[566, 578], [-335, -315]]
    # Define the speed sign place
    Speed_sign1 = [[351, 371], [-577, -565]]
    Speed_sign2 = [[266.5, 278.5], [-430, -410]]
    # Define the pedstranian sign place
    Ped_sign1 = [[266.5, 278.5], [-508, -490]]
    Ped_sign2 = [[385, 400], [-353, -341]]
    
    # Define road lane boundaries to compute deviation from the road.
    Deviation1 = [[1000, 266], [-577, -565]]
    Deviation2 = [[266.5, 278.5], [-564, -354]]
    Deviation3 = [[279, 565], [-353, -341]]
    Deviation4 = [[566, 578], [-340, 500]]

    ContinousPerf = []
    LastContPerf = 1
    CrossedSpeedSign1 = False
    CrossedSpeedSign2 = False
    CrossedPedSign1 = False
    CrossedPedSign2 = False
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
    
    cnt = 0
    for l in data:
        
        # Data extraction.
        x, y, Speed = l[0], l[1], l[2] 

        cnt+=1
        #------------------------------- turning performance part-------------------------------------
        TurnPerfTemp,crossedTurn1 = VerticalTurnLRFromLRLane(line1_1, line1_2, crossedTurn1, x, y)
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
        PedPerf1,CrossedPedSign1 = PedstranianSignRight(Ped_sign1, CrossedPedSign1, x, y, Speed, PedPerf1)
        PedPerf2,CrossedPedSign2 = PedstranianSignUp(Ped_sign2, CrossedPedSign2, x, y, Speed, PedPerf2)
    
        #------------------------------- continous deviation performance part-------------------------------------
        if(crossedTurn1 or crossedTurn2 or crossedTurn3):
            ContinousPerf.append([time,LastContPerf])
            TotalDevPerf+=LastContPerf
            continue
        LastContPerfTemp1 = MovVerticalLeftLane(Deviation1,x,y)
        LastContPerfTemp2 = MovHorizontalDownLane(Deviation2,x,y)
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
    DevPerf = math.ceil(TotalDevPerf/(cnt))
    TurnPerfTotal = math.ceil(sum(TurnPerf))
    SpeedPerfTotal = math.ceil((SpeedPerf1+SpeedPerf2))
    PedPerfTotal = math.ceil((PedPerf1+PedPerf2))
    print("performance turn: " + str(TurnPerfTotal))
    print("performance speed1: " + str(SpeedPerf1))
    print("performance speed2: " + str(SpeedPerf2))
    print("performance ped1: " + str(PedPerf1))
    print("performance ped2: " + str(PedPerf2))
    print("performance stop: " + str(StopPerf)) 
    print("performance deviation: " + str(DevPerf))
    return ( DevPerf + SpeedPerfTotal + PedPerfTotal + TurnPerfTotal ) /8, ContinousPerf

