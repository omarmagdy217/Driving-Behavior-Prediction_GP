
import os.path as path
import time
import math

import Final_performan_escripts.rank2_road1 as road1
import Final_performan_escripts.rank3_road1 as road2
import Final_performan_escripts.rank1_road1 as road3
import Final_performan_escripts.rank2_road2 as road4
import Final_performan_escripts.rank2_road3 as road5
import Final_performan_escripts.rank1_road2 as road6

log_path = path.expanduser('~\\Documents\\AirSim\\airsim_rec.txt')

curDataIndex = 0
data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []

RankSplit1 = [[366, 378], [-380, -360]]
RankSplit2 = [[475, 495], [-394, -382]]
RankSplit3 = [[642, 654], [-870, -850]]
RankSplit4 = [[390, 410], [-577, -565]]
RankSplit5 = [[566.5, 578.5], [-335, -300]]


def compute():
    with open(log_path, 'r') as f:

        cnt = 0
        curDataIndex = 0
        for l in f.readlines():

            line = l.split()
            # Check whether the line is empty.
            if(len(line) == 0 or cnt == 0):
                cnt += 1
                continue
            cnt = cnt + 1
            # Data extraction.
            time, x, y, z, Q_W,	Q_X, Q_Y, Q_Z, Throttle, Steering, Brake, Gear, Handbrake, RPM, Speed = float(line[0]), float(line[1]), float(line[2]), float(line[3]), float(
                line[4]), float(line[5]), float(line[6]), float(line[7]), float(line[8]), float(line[9]), float(line[10]), float(line[11]), float(line[12]), float(line[13]), float(line[14])
            if(RankSplit1[0][0] <= x <= RankSplit1[0][1] and RankSplit1[1][0] <= y <= RankSplit1[1][1]):
                curDataIndex = 1
            elif(RankSplit2[0][0] <= x <= RankSplit2[0][1] and RankSplit2[1][0] <= y <= RankSplit2[1][1]):
                curDataIndex = 2
            elif(RankSplit3[0][0] <= x <= RankSplit3[0][1] and RankSplit3[1][0] <= y <= RankSplit3[1][1]):
                curDataIndex = 3
            elif(RankSplit4[0][0] <= x <= RankSplit4[0][1] and RankSplit4[1][0] <= y <= RankSplit4[1][1]):
                curDataIndex = 4
            elif(RankSplit5[0][0] <= x <= RankSplit5[0][1] and RankSplit5[1][0] <= y <= RankSplit5[1][1]):
                curDataIndex = 5

            if(curDataIndex == 0):
                data1.append([x, y, Speed])
            elif(curDataIndex == 1):
                data2.append([x, y, Speed])
            elif(curDataIndex == 2):
                data3.append([x, y, Speed])
            elif(curDataIndex == 3):
                data4.append([x, y, Speed])
            elif(curDataIndex == 4):
                data5.append([x, y, Speed])
            elif(curDataIndex == 5):
                data6.append([x, y, Speed])

    p1 = road1.analyse(data1)
    p2 = road2.analyse(data2)
    p3 = road3.analyse(data3)
    p4 = road4.analyse(data4)
    p5 = road5.analyse(data5)
    p6 = road6.analyse(data6)
    # Map output from 1->5 to 0%->100%
    return [round(100-((x-1)*25)) for x in [p1, p2, p3, p4, p5, p6]]


print(compute())
