# Helper function to get the speed sign performance. 
def SpeedSign(speedPlace, flag, x, y, Speed, prev_perf, curSpeed):
    if(speedPlace[0][0] <= x <= speedPlace[0][1] and speedPlace[1][0] <= y <= speedPlace[1][1]):
        flag = True
    if(flag and Speed>curSpeed and Speed<=curSpeed+3 and prev_perf<2):
        return 2,flag
    if(flag and Speed>curSpeed+3 and Speed<curSpeed+5 and prev_perf<3):
        return 3,flag
    if(flag and Speed>=curSpeed+5 and Speed<=curSpeed+10 and prev_perf<4):
        return 4,flag
    if(flag and Speed>curSpeed+10 and prev_perf<5):
        return 5,flag
    return prev_perf,flag    