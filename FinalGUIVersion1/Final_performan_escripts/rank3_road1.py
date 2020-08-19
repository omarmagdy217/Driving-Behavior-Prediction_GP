import os.path as path
import time
import math
from Final_performan_escripts.TurningPerf import *
from Final_performan_escripts.speedPerf import *
from Final_performan_escripts.stopPerf import *
from Final_performan_escripts.ContinousPerf import *
from Final_performan_escripts.PedstranianPerf import *


def analyse(data):
    if len(data) == 0:
        return 0
    # Define road stripes for first square.
    line1_1 = [[369.5, 381.5], [-448, -430]]
    line1_2 = [[390, 405], [-462.5, -450.5]]
    # Define road stripes for second square.
    line2_1 = [[495, 510], [-462.5, -450.5]]
    line2_2 = [[514.5, 526.5], [-443, -425]]
    # Define road stripes for third square.
    line3_1 = [[513, 525], [-315, -299]]
    line3_2 = [[490, 505], [-297, -285]]
    # Define road stripes for four square.
    line4_1 = [[389, 405], [-297, -285]]
    line4_2 = [[373, 385], [-318, -303]]
    # Define road stripes for fifth square.
    line5_1 = [[374, 386], [-382, -365]]
    line5_2 = [[391, 415], [-398, -386]]
    # Define the speed sign place
    Speed_sign1 = [[369.5, 381.5], [-410, -395]]
    Speed_sign2 = [[513, 525], [-450, -430]]
    Speed_sign3 = [[373, 385], [-325, -310]]
    # Define the pedstranian sign place
    Ped_sign1 = [[450, 465], [-462.5, -450.5]]
    Ped_sign2 = [[513, 525], [-350, -335]]
    Ped_sign3 = [[480, 465], [-297, -285]]
    Ped_sign4 = [[373, 385], [-365, -340]]
    # Define road lane boundaries to compute deviation from the road.
    Deviation1 = [[369.5, 381.5], [-450, 0]]
    Deviation2 = [[382, 512], [-462.5, -450.5]]
    Deviation3 = [[513, 525], [-450, -296]]
    Deviation4 = [[372, 512], [-297, -285]]
    Deviation5 = [[373, 385], [-385, -298]]
    Deviation6 = [[386, 800], [-398, -386]]

    ContinousPerf = []
    LastContPerf = 1
    CrossedSpeedSign1 = False
    CrossedSpeedSign2 = False
    CrossedSpeedSign3 = False
    CrossedPedSign1 = False
    CrossedPedSign2 = False
    CrossedPedSign3 = False
    CrossedPedSign4 = False
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
    cnt = 0
    for l in data:

        # Data extraction.
        x, y, Speed = l[0], l[1], l[2]

        cnt += 1
        # ------------------------------- turning performance part-------------------------------------
        TurnPerfTemp, crossedTurn1 = HorizontalTurnLRFromRLLane(
            line1_1, line1_2, crossedTurn1, x, y)
        if(TurnPerfTemp != 0):
            TurnPerf.append(TurnPerfTemp)

        TurnPerfTemp2, crossedTurn2 = VerticalTurnLRFromLRLane(
            line2_1, line2_2, crossedTurn2, x, y)
        if(TurnPerfTemp2 != 0):
            TurnPerf.append(TurnPerfTemp2)

        TurnPerfTemp3, crossedTurn3 = HorizontalTurnLRFromLRLane(
            line3_1, line3_2, crossedTurn3, x, y)
        if(TurnPerfTemp3 != 0):
            TurnPerf.append(TurnPerfTemp3)

        TurnPerfTemp4, crossedTurn4 = VerticalTurnLRFromRLLane(
            line4_1, line4_2, crossedTurn4, x, y)
        if(TurnPerfTemp4 != 0):
            TurnPerf.append(TurnPerfTemp4)

        TurnPerfTemp5, crossedTurn5 = HorizontalTurnLRFromRLLane(
            line5_1, line5_2, crossedTurn5, x, y)
        if(TurnPerfTemp5 != 0):
            TurnPerf.append(TurnPerfTemp5)

        # ------------------------------- Speed limit performance part-------------------------------------
        SpeedPerf1, CrossedSpeedSign1 = SpeedSign(
            Speed_sign1, CrossedSpeedSign1, x, y, Speed, SpeedPerf1, 20)
        SpeedPerf2, CrossedSpeedSign2 = SpeedSign(
            Speed_sign2, CrossedSpeedSign2, x, y, Speed, SpeedPerf2, 30)
        SpeedPerf3, CrossedSpeedSign3 = SpeedSign(
            Speed_sign3, CrossedSpeedSign3, x, y, Speed, SpeedPerf3, 20)
        if(CrossedSpeedSign2):
            CrossedSpeedSign1 = False
        if(CrossedSpeedSign3):
            CrossedSpeedSign2 = False
        # ------------------------------- Pedstranian sign performance part-------------------------------------
        PedPerf1, CrossedPedSign1 = PedstranianSignUp(
            Ped_sign1, CrossedPedSign1, x, y, Speed, PedPerf1)
        PedPerf2, CrossedPedSign2 = PedstranianSignRight(
            Ped_sign2, CrossedPedSign2, x, y, Speed, PedPerf2)
        PedPerf3, CrossedPedSign3 = PedstranianSignDown(
            Ped_sign3, CrossedPedSign3, x, y, Speed, PedPerf3)
        PedPerf4, CrossedPedSign4 = PedstranianSignLeft(
            Ped_sign4, CrossedPedSign4, x, y, Speed, PedPerf4)

        # ------------------------------- continous deviation performance part-------------------------------------
        if(crossedTurn1 or crossedTurn2 or crossedTurn3 or crossedTurn4 or crossedTurn5):
            ContinousPerf.append([time, LastContPerf])
            TotalDevPerf += LastContPerf
            continue
        LastContPerfTemp1 = MovHorizontalupLane(Deviation1, x, y)
        LastContPerfTemp2 = MovVerticalRightLane(Deviation2, x, y)
        LastContPerfTemp3 = MovHorizontalDownLane(Deviation3, x, y)
        LastContPerfTemp4 = MovVerticalLeftLane(Deviation4, x, y)
        LastContPerfTemp5 = MovHorizontalupLane(Deviation5, x, y)
        LastContPerfTemp6 = MovVerticalRightLane(Deviation6, x, y)
        if(LastContPerfTemp1 != 0):
            LastContPerf = LastContPerfTemp1
            ContinousPerf.append([time, LastContPerf])
        if(LastContPerfTemp2 != 0):
            LastContPerf = LastContPerfTemp2
            ContinousPerf.append([time, LastContPerf])
        if(LastContPerfTemp3 != 0):
            LastContPerf = LastContPerfTemp3
            ContinousPerf.append([time, LastContPerf])
        if(LastContPerfTemp4 != 0):
            LastContPerf = LastContPerfTemp4
            ContinousPerf.append([time, LastContPerf])
        if(LastContPerfTemp5 != 0):
            LastContPerf = LastContPerfTemp5
            ContinousPerf.append([time, LastContPerf])
        if(LastContPerfTemp6 != 0):
            LastContPerf = LastContPerfTemp6
            ContinousPerf.append([time, LastContPerf])
        TotalDevPerf += LastContPerf
# =============================================result================================================
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
    print("performance deviation: " + str(DevPerf) + "\n")
    return (DevPerf + SpeedPerfTotal + PedPerfTotal + TurnPerfTotal) / 13
