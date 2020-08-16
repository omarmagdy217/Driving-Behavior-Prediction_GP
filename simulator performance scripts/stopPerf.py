# Helper function to get the stop sign performance with moving left. 
def StopSignLeft(stopPlace, flag, x, y, Speed, prev_perf):
    place = stopPlace[1][0]
    Boundary1 = [[stopPlace[0][0], stopPlace[0][1]], [place-15, place-10]]
    Boundary2 = [[stopPlace[0][0], stopPlace[0][1]], [place-20, place-15]]
    Boundary3 = [[stopPlace[0][0], stopPlace[0][1]], [place-25, place-20]]
    Boundary4 = [[stopPlace[0][0], stopPlace[0][1]], [place-100, place-25]]
    if(stopPlace[0][0] <= x <= stopPlace[0][1] and stopPlace[1][0] <= y <= stopPlace[1][1]):
        flag = True
    if(flag and Boundary1[0][0] <= x <= Boundary1[0][1] and Boundary1[1][0] <= y <= Boundary1[1][1] and Speed>5 and prev_perf<2):
        return 2,flag    
    if(flag and Boundary2[0][0] <= x <= Boundary2[0][1] and Boundary2[1][0] <= y <= Boundary2[1][1] and Speed > 5 and prev_perf < 3):
        return 3,flag
    if(flag and Boundary3[0][0] <= x <= Boundary3[0][1] and Boundary3[1][0] <= y <= Boundary3[1][1] and Speed > 5 and prev_perf < 4):
        return 4,flag
    if(flag and Boundary4[0][0] <= x <= Boundary4[0][1] and Boundary4[1][0] <= y <= Boundary4[1][1] and Speed > 5 and prev_perf < 5):
        return 5,flag
    return prev_perf,flag 


# Helper function to get the stop sign performance with moving left. 
def StopSignRight(stopPlace, flag, x, y, Speed, prev_perf):
    place = stopPlace[1][1]
    Boundary1 = [[stopPlace[0][0], stopPlace[0][1]], [place+10, place+15]]
    Boundary2 = [[stopPlace[0][0], stopPlace[0][1]], [place+15, place+20]]
    Boundary3 = [[stopPlace[0][0], stopPlace[0][1]], [place+20, place+25]]
    Boundary4 = [[stopPlace[0][0], stopPlace[0][1]], [place+25, place+100]]
    if(stopPlace[0][0] <= x <= stopPlace[0][1] and stopPlace[1][0] <= y <= stopPlace[1][1]):
        flag = True
    if(flag and Boundary1[0][0] <= x <= Boundary1[0][1] and Boundary1[1][0] <= y <= Boundary1[1][1] and Speed>5 and prev_perf<2):
        return 2,flag    
    if(flag and Boundary2[0][0] <= x <= Boundary2[0][1] and Boundary2[1][0] <= y <= Boundary2[1][1] and Speed > 5 and prev_perf < 3):
        return 3,flag
    if(flag and Boundary3[0][0] <= x <= Boundary3[0][1] and Boundary3[1][0] <= y <= Boundary3[1][1] and Speed > 5 and prev_perf < 4):
        return 4,flag
    if(flag and Boundary4[0][0] <= x <= Boundary4[0][1] and Boundary4[1][0] <= y <= Boundary4[1][1] and Speed > 5 and prev_perf < 5):
        return 5,flag
    return prev_perf,flag 

# Helper function to get the stop sign performance with moving Down. 
def StopSignDown(stopPlace, flag, x, y, Speed, prev_perf):
    place = stopPlace[0][0]
    Boundary1 = [[place-15, place-10], [stopPlace[1][0], stopPlace[1][1]]]
    Boundary2 = [[place-20, place-15], [stopPlace[1][0], stopPlace[1][1]]]
    Boundary3 = [[place-25, place-20], [stopPlace[1][0], stopPlace[1][1]]]
    Boundary4 = [[place-100, place-25], [stopPlace[1][0], stopPlace[1][1]]]
    if(stopPlace[0][0] <= x <= stopPlace[0][1] and stopPlace[1][0] <= y <= stopPlace[1][1]):
        flag = True
    if(flag and Boundary1[0][0] <= x <= Boundary1[0][1] and Boundary1[1][0] <= y <= Boundary1[1][1] and Speed>5 and prev_perf<2):
        return 2,flag    
    if(flag and Boundary2[0][0] <= x <= Boundary2[0][1] and Boundary2[1][0] <= y <= Boundary2[1][1] and Speed > 5 and prev_perf < 3):
        return 3,flag
    if(flag and Boundary3[0][0] <= x <= Boundary3[0][1] and Boundary3[1][0] <= y <= Boundary3[1][1] and Speed > 5 and prev_perf < 4):
        return 4,flag
    if(flag and Boundary4[0][0] <= x <= Boundary4[0][1] and Boundary4[1][0] <= y <= Boundary4[1][1] and Speed > 5 and prev_perf < 5):
        return 5,flag
    return prev_perf,flag 

# Helper function to get the stop sign performance with moving Down. 
def StopSignUp(stopPlace, flag, x, y, Speed, prev_perf):
    place = stopPlace[0][0]
    Boundary1 = [[place+10, place+15], [stopPlace[1][0], stopPlace[1][1]]]
    Boundary2 = [[place+15, place+20], [stopPlace[1][0], stopPlace[1][1]]]
    Boundary3 = [[place+20, place+25], [stopPlace[1][0], stopPlace[1][1]]]
    Boundary4 = [[place+25, place+100], [stopPlace[1][0], stopPlace[1][1]]]
    if(stopPlace[0][0] <= x <= stopPlace[0][1] and stopPlace[1][0] <= y <= stopPlace[1][1]):
        flag = True
    if(flag and Boundary1[0][0] <= x <= Boundary1[0][1] and Boundary1[1][0] <= y <= Boundary1[1][1] and Speed>5 and prev_perf<2):
        return 2,flag    
    if(flag and Boundary2[0][0] <= x <= Boundary2[0][1] and Boundary2[1][0] <= y <= Boundary2[1][1] and Speed > 5 and prev_perf < 3):
        return 3,flag
    if(flag and Boundary3[0][0] <= x <= Boundary3[0][1] and Boundary3[1][0] <= y <= Boundary3[1][1] and Speed > 5 and prev_perf < 4):
        return 4,flag
    if(flag and Boundary4[0][0] <= x <= Boundary4[0][1] and Boundary4[1][0] <= y <= Boundary4[1][1] and Speed > 5 and prev_perf < 5):
        return 5,flag
    return prev_perf,flag     