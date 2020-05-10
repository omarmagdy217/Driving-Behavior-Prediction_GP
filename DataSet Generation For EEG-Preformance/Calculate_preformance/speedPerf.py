# Helper function to get the speed sign performance. 
def SpeedSign(speedPlace, flag, x, y, Speed, prev_perf):
    if(speedPlace[0][0] <= x <= speedPlace[0][1] and speedPlace[1][0] <= y <= speedPlace[1][1]):
        flag = True
    if(flag and Speed>20 and Speed<=23 and prev_perf<2):
        return 2,flag
    if(flag and Speed>23 and Speed<25 and prev_perf<3):
        return 3,flag
    if(flag and Speed>=25 and Speed<=30 and prev_perf<4):
        return 4,flag
    if(flag and Speed>30 and prev_perf<5):
        return 5,flag
    return prev_perf,flag    