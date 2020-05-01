# Helper function to get the turning performance with moving in upward right lane and 
# turn left, or left lane and turn right. 
def VerticalTurnLRFromRLLane(line1, line2, flag, x, y):
    laneWidth = abs(line2[0][0]-line2[0][1])
    half = line2[0][0] + laneWidth/2 + laneWidth/4
    Rang1_1 = [[half-2, half],[ line2[1][0], line2[1][1] ]]
    Rang1_2 = [[half, half+0.5],[ line2[1][0], line2[1][1] ]]

    Rang2_1 = [[half-3, half-2],[ line2[1][0], line2[1][1] ]]
    Rang2_2 = [[half+0.5, half+1.5],[ line2[1][0], line2[1][1] ]]

    Rang3_1 = [[half-4, half-3],[ line2[1][0], line2[1][1] ]]
    Rang3_2 = [[half+1.5, half+2],[ line2[1][0], line2[1][1] ]]
    
    Rang4_1 = [[half-5, half-4],[ line2[1][0], line2[1][1] ]]
    Rang4_2 = [[half+2, half+3],[ line2[1][0], line2[1][1] ]]

    Rang5_1 = [[half-7, half-5],[ line2[1][0], line2[1][1] ]]
    Rang5_2 = [[half+3, half+10],[ line2[1][0], line2[1][1] ]]

    if(line1[0][0] <= x <= line1[0][1] and line1[1][0] <= y <= line1[1][1]):	    
        flag = True
    if(line2[0][0] <= x <= line2[0][1] and line2[1][0] <= y <= line2[1][1] and flag):
        if(Rang1_1[0][0] <= x <= Rang1_1[0][1] and Rang1_1[1][0] <= y <= Rang1_1[1][1]):
            flag = False
            return 1,flag
        elif(Rang1_2[0][0] <= x <= Rang1_2[0][1] and Rang1_2[1][0] <= y <= Rang1_2[1][1]):
            flag = False
            return 1,flag
        elif(Rang2_1[0][0] <= x <= Rang2_1[0][1] and Rang2_1[1][0] <= y <= Rang2_1[1][1]):
            flag = False
            return 2,flag
        elif(Rang2_2[0][0] <= x <= Rang2_2[0][1] and Rang2_2[1][0] <= y <= Rang2_2[1][1]):
            flag = False
            return 2,flag
        elif(Rang3_1[0][0] <= x <= Rang3_1[0][1] and Rang3_1[1][0] <= y <= Rang3_1[1][1]):
            flag = False
            return 3,flag
        elif(Rang3_2[0][0] <= x <= Rang3_2[0][1] and Rang3_2[1][0] <= y <= Rang3_2[1][1]):
            flag = False
            return 3,flag
        elif(Rang4_1[0][0] <= x <= Rang4_1[0][1] and Rang4_1[1][0] <= y <= Rang4_1[1][1]):
            flag = False
            return 4,flag
        elif(Rang4_2[0][0] <= x <= Rang4_2[0][1] and Rang4_2[1][0] <= y <= Rang4_2[1][1]):
            flag = False
            return 4,flag
        elif(Rang5_1[0][0] <= x <= Rang5_1[0][1] and Rang5_1[1][0] <= y <= Rang5_1[1][1]):
            flag = False
            return 5,flag
        elif(Rang5_2[0][0] <= x <= Rang5_2[0][1] and Rang5_2[1][0] <= y <= Rang5_2[1][1]):
            flag = False
            return 5,flag
    return 0,flag


# Helper function to get the turning performance with moving in upward left lane and 
# turn left, or right lane and turn right. 
def VerticalTurnLRFromLRLane(line1, line2, flag, x, y):
    laneWidth = abs(line2[0][0]-line2[0][1])
    half = line2[0][0] + laneWidth/4
    Rang1_1 = [[half-0.5, half],[ line2[1][0], line2[1][1] ]]
    Rang1_2 = [[half, half+2],[ line2[1][0], line2[1][1] ]]

    Rang2_1 = [[half-1.5, half-0.5],[ line2[1][0], line2[1][1] ]]
    Rang2_2 = [[half+2, half+3],[ line2[1][0], line2[1][1] ]]

    Rang3_1 = [[half-2, half-1.5],[ line2[1][0], line2[1][1] ]]
    Rang3_2 = [[half+3, half+4],[ line2[1][0], line2[1][1] ]]
    
    Rang4_1 = [[half-3, half-2],[ line2[1][0], line2[1][1] ]]
    Rang4_2 = [[half+4, half+5],[ line2[1][0], line2[1][1] ]]

    Rang5_1 = [[half-13, half-3],[ line2[1][0], line2[1][1] ]]
    Rang5_2 = [[half+5, half+10],[ line2[1][0], line2[1][1] ]]

    if(line1[0][0] <= x <= line1[0][1] and line1[1][0] <= y <= line1[1][1]):	    
        flag = True
    if(line2[0][0] <= x <= line2[0][1] and line2[1][0] <= y <= line2[1][1] and flag):
        if(Rang1_1[0][0] <= x <= Rang1_1[0][1] and Rang1_1[1][0] <= y <= Rang1_1[1][1]):
            flag = False
            return 1,flag
        elif(Rang1_2[0][0] <= x <= Rang1_2[0][1] and Rang1_2[1][0] <= y <= Rang1_2[1][1]):
            flag = False
            return 1,flag
        elif(Rang2_1[0][0] <= x <= Rang2_1[0][1] and Rang2_1[1][0] <= y <= Rang2_1[1][1]):
            flag = False
            return 2,flag
        elif(Rang2_2[0][0] <= x <= Rang2_2[0][1] and Rang2_2[1][0] <= y <= Rang2_2[1][1]):
            flag = False
            return 2,flag
        elif(Rang3_1[0][0] <= x <= Rang3_1[0][1] and Rang3_1[1][0] <= y <= Rang3_1[1][1]):
            flag = False
            return 3,flag
        elif(Rang3_2[0][0] <= x <= Rang3_2[0][1] and Rang3_2[1][0] <= y <= Rang3_2[1][1]):
            flag = False
            return 3,flag
        elif(Rang4_1[0][0] <= x <= Rang4_1[0][1] and Rang4_1[1][0] <= y <= Rang4_1[1][1]):
            flag = False
            return 4,flag
        elif(Rang4_2[0][0] <= x <= Rang4_2[0][1] and Rang4_2[1][0] <= y <= Rang4_2[1][1]):
            flag = False
            return 4,flag
        elif(Rang5_1[0][0] <= x <= Rang5_1[0][1] and Rang5_1[1][0] <= y <= Rang5_1[1][1]):
            flag = False
            return 5,flag
        elif(Rang5_2[0][0] <= x <= Rang5_2[0][1] and Rang5_2[1][0] <= y <= Rang5_2[1][1]):
            flag = False
            return 5,flag
    return 0,flag


# Helper function to get the turning performance with moving in rightward Left lane and 
# turn right, or right lane and turn left. 
def HorizontalTurnLRFromRLLane(line1, line2, flag, x, y):
    laneWidth = abs(line2[1][0]-line2[1][1])
    half = line2[1][0] + laneWidth/2 + laneWidth/4
    Rang1_1 = [[line2[0][0], line2[0][1]],[ half,half+0.5]]
    Rang1_2 = [[line2[0][0], line2[0][1]],[ half-2,half ]]

    Rang2_1 = [[line2[0][0], line2[0][1]],[ half+0.5,half+1.5 ]]
    Rang2_2 = [[line2[0][0], line2[0][1]],[ half-3,half-2 ]]

    Rang3_1 = [[line2[0][0], line2[0][1]],[ half+1.5,half+2 ]]
    Rang3_2 = [[line2[0][0], line2[0][1]],[ half-4,half-3 ]]
    
    Rang4_1 = [[line2[0][0], line2[0][1]],[ half+2,half+3 ]]
    Rang4_2 = [[line2[0][0], line2[0][1]],[ half-5, half-4]]

    Rang5_1 = [[line2[0][0], line2[0][1]],[ half+3,half+10 ]]
    Rang5_2 = [[line2[0][0], line2[0][1]],[ half-10,half-5 ]]

    if(line1[0][0] <= x <= line1[0][1] and line1[1][0] <= y <= line1[1][1]):	    
        flag = True
    if(line2[0][0] <= x <= line2[0][1] and line2[1][0] <= y <= line2[1][1] and flag):
        if(Rang1_1[0][0] <= x <= Rang1_1[0][1] and Rang1_1[1][0] <= y <= Rang1_1[1][1]):
            flag = False
            return 1,flag
        elif(Rang1_2[0][0] <= x <= Rang1_2[0][1] and Rang1_2[1][0] <= y <= Rang1_2[1][1]):
            flag = False
            return 1,flag
        elif(Rang2_1[0][0] <= x <= Rang2_1[0][1] and Rang2_1[1][0] <= y <= Rang2_1[1][1]):
            flag = False
            return 2,flag
        elif(Rang2_2[0][0] <= x <= Rang2_2[0][1] and Rang2_2[1][0] <= y <= Rang2_2[1][1]):
            flag = False
            return 2,flag
        elif(Rang3_1[0][0] <= x <= Rang3_1[0][1] and Rang3_1[1][0] <= y <= Rang3_1[1][1]):
            flag = False
            return 3,flag
        elif(Rang3_2[0][0] <= x <= Rang3_2[0][1] and Rang3_2[1][0] <= y <= Rang3_2[1][1]):
            flag = False
            return 3,flag
        elif(Rang4_1[0][0] <= x <= Rang4_1[0][1] and Rang4_1[1][0] <= y <= Rang4_1[1][1]):
            flag = False
            return 4,flag
        elif(Rang4_2[0][0] <= x <= Rang4_2[0][1] and Rang4_2[1][0] <= y <= Rang4_2[1][1]):
            flag = False
            return 4,flag
        elif(Rang5_1[0][0] <= x <= Rang5_1[0][1] and Rang5_1[1][0] <= y <= Rang5_1[1][1]):
            flag = False
            return 5,flag
        elif(Rang5_2[0][0] <= x <= Rang5_2[0][1] and Rang5_2[1][0] <= y <= Rang5_2[1][1]):
            flag = False
            return 5,flag
    return 0,flag


# Helper function to get the turning performance with moving in rightward Left lane and 
# turn left, or right lane and turn right.
def HorizontalTurnLRFromLRLane(line1, line2, flag, x, y):
    laneWidth = abs(line2[1][0]-line2[1][1])
    half = line2[1][0] + laneWidth/4
    Rang1_1 = [[line2[0][0], line2[0][1]],[ half-0.5,half]]
    Rang1_2 = [[line2[0][0], line2[0][1]],[ half,half+2 ]]

    Rang2_1 = [[line2[0][0], line2[0][1]],[ half-1.5,half-0.5 ]]
    Rang2_2 = [[line2[0][0], line2[0][1]],[ half+2,half+3 ]]

    Rang3_1 = [[line2[0][0], line2[0][1]],[ half-2,half-1.5 ]]
    Rang3_2 = [[line2[0][0], line2[0][1]],[ half+3,half+4 ]]
    
    Rang4_1 = [[line2[0][0], line2[0][1]],[ half-3,half-2 ]]
    Rang4_2 = [[line2[0][0], line2[0][1]],[ half+4, half+5]]

    Rang5_1 = [[line2[0][0], line2[0][1]],[ half-10,half-3 ]]
    Rang5_2 = [[line2[0][0], line2[0][1]],[ half+5,half+10 ]]

    if(line1[0][0] <= x <= line1[0][1] and line1[1][0] <= y <= line1[1][1]):        
        flag = True
    if(line2[0][0] <= x <= line2[0][1] and line2[1][0] <= y <= line2[1][1] and flag):
        if(Rang1_1[0][0] <= x <= Rang1_1[0][1] and Rang1_1[1][0] <= y <= Rang1_1[1][1]):
            flag = False
            return 1,flag
        elif(Rang1_2[0][0] <= x <= Rang1_2[0][1] and Rang1_2[1][0] <= y <= Rang1_2[1][1]):
            flag = False
            return 1,flag
        elif(Rang2_1[0][0] <= x <= Rang2_1[0][1] and Rang2_1[1][0] <= y <= Rang2_1[1][1]):
            flag = False
            return 2,flag
        elif(Rang2_2[0][0] <= x <= Rang2_2[0][1] and Rang2_2[1][0] <= y <= Rang2_2[1][1]):
            flag = False
            return 2,flag
        elif(Rang3_1[0][0] <= x <= Rang3_1[0][1] and Rang3_1[1][0] <= y <= Rang3_1[1][1]):
            flag = False
            return 3,flag
        elif(Rang3_2[0][0] <= x <= Rang3_2[0][1] and Rang3_2[1][0] <= y <= Rang3_2[1][1]):
            flag = False
            return 3,flag
        elif(Rang4_1[0][0] <= x <= Rang4_1[0][1] and Rang4_1[1][0] <= y <= Rang4_1[1][1]):
            flag = False
            return 4,flag
        elif(Rang4_2[0][0] <= x <= Rang4_2[0][1] and Rang4_2[1][0] <= y <= Rang4_2[1][1]):
            flag = False
            return 4,flag
        elif(Rang5_1[0][0] <= x <= Rang5_1[0][1] and Rang5_1[1][0] <= y <= Rang5_1[1][1]):
            flag = False
            return 5,flag
        elif(Rang5_2[0][0] <= x <= Rang5_2[0][1] and Rang5_2[1][0] <= y <= Rang5_2[1][1]):
            flag = False
            return 5,flag
    return 0,flag