import os.path as path
import time
import math
from Final_performan_escripts.TurningPerf import *
from Final_performan_escripts.speedPerf import *
from Final_performan_escripts.stopPerf import *
from Final_performan_escripts.ContinousPerf import *


def analyse(data):
    if len(data) == 0:
        return 0
    # Define road stripes for first square.
    line1_1 = [[620, 640], [-394, -382]]
    line1_2 = [[642, 654], [-415, -395]]
    # Define the speed sign place
    Speed_sign = [[642, 654], [-500, -475]]
    # Define road lane boundaries to compute deviation from the road.
    Deviation1 = [[0, 641], [-394, -382]]
    Deviation2 = [[642, 654], [-800, -395]]

    ContinousPerf = []
    LastContPerf = 1
    CrossedSpeedSign = False
    crossedTurn1 = False

    TurnPerf = []
    SpeedPerf = 1
    TotalDevPerf = 0

    cnt = 0
    for l in data:

        # Data extraction.
        x, y, Speed = l[0], l[1], l[2]

        cnt += 1
        # ------------------------------- turning performance part-------------------------------------
        TurnPerfTemp, crossedTurn1 = VerticalTurnLRFromRLLane(
            line1_1, line1_2, crossedTurn1, x, y)
        if(TurnPerfTemp != 0):
            TurnPerf.append(TurnPerfTemp)

        # ------------------------------- Speed limit performance part-------------------------------------
        SpeedPerf, CrossedSpeedSign = SpeedSign(
            Speed_sign, CrossedSpeedSign, x, y, Speed, SpeedPerf, 20)

        # ------------------------------- continous deviation performance part-------------------------------------
        if(crossedTurn1):
            ContinousPerf.append([time, LastContPerf])
            TotalDevPerf += LastContPerf
            continue
        LastContPerfTemp1 = MovVerticalLeftLane(Deviation1, x, y)
        LastContPerfTemp2 = MovHorizontalDownLane(Deviation2, x, y)
        if(LastContPerfTemp1 != 0):
            LastContPerf = LastContPerfTemp1
            ContinousPerf.append([time, LastContPerf])
        if(LastContPerfTemp2 != 0):
            LastContPerf = LastContPerfTemp2
            ContinousPerf.append([time, LastContPerf])
        TotalDevPerf += LastContPerf
# =============================================result================================================
    DevPerf = math.ceil(TotalDevPerf/(cnt))
    print("performance turn: " + str(sum(TurnPerf)))
    print("performance speed: " + str(SpeedPerf))
    print("performance deviation: " + str(DevPerf) + "\n")
    return (DevPerf+SpeedPerf+sum(TurnPerf))/3
