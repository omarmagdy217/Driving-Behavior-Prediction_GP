# Helper function to get the pedstranian sign performance with moving left. 
def PedstranianSignLeft(stopPlace, flag, x, y, Speed, prev_perf):
    place = stopPlace[1][0]
    Boundary1 = [[stopPlace[0][0], stopPlace[0][1]], [place-13, place-3]]
    Boundary2 = [[stopPlace[0][0], stopPlace[0][1]], [place-23, place-13]]
    Boundary3 = [[stopPlace[0][0], stopPlace[0][1]], [place-33, place-23]]
    Boundary4 = [[stopPlace[0][0], stopPlace[0][1]], [place-100, place-33]]
    if(stopPlace[0][0] <= x <= stopPlace[0][1] and stopPlace[1][0] <= y <= stopPlace[1][1]):
        flag = True
    if(flag and Speed <= 5):
        flag = False
        return prev_perf,flag    
    if(flag and Boundary1[0][0] <= x <= Boundary1[0][1] and Boundary1[1][0] <= y <= Boundary1[1][1] and Speed>5 and prev_perf<2):
        return 2,flag    
    if(flag and Boundary2[0][0] <= x <= Boundary2[0][1] and Boundary2[1][0] <= y <= Boundary2[1][1] and Speed > 5 and prev_perf < 3):
        return 3,flag
    if(flag and Boundary3[0][0] <= x <= Boundary3[0][1] and Boundary3[1][0] <= y <= Boundary3[1][1] and Speed > 5 and prev_perf < 4):
        return 4,flag
    if(flag and Boundary4[0][0] <= x <= Boundary4[0][1] and Boundary4[1][0] <= y <= Boundary4[1][1] and Speed > 5 and prev_perf < 5):
        flag = False
        return 5,flag
    return prev_perf,flag 


# Helper function to get the pedstranian sign performance with moving right. 
def PedstranianSignRight(stopPlace, flag, x, y, Speed, prev_perf):
    place = stopPlace[1][1]
    Boundary1 = [[stopPlace[0][0], stopPlace[0][1]], [place+3, place+13]]
    Boundary2 = [[stopPlace[0][0], stopPlace[0][1]], [place+13, place+23]]
    Boundary3 = [[stopPlace[0][0], stopPlace[0][1]], [place+23, place+33]]
    Boundary4 = [[stopPlace[0][0], stopPlace[0][1]], [place+33, place+100]]
    if(stopPlace[0][0] <= x <= stopPlace[0][1] and stopPlace[1][0] <= y <= stopPlace[1][1]):
        flag = True
    if(flag and Speed<=5):
        flag = False
        return prev_perf,flag    
    if(flag and Boundary1[0][0] <= x <= Boundary1[0][1] and Boundary1[1][0] <= y <= Boundary1[1][1] and Speed>5 and prev_perf<2):
        return 2,flag    
    if(flag and Boundary2[0][0] <= x <= Boundary2[0][1] and Boundary2[1][0] <= y <= Boundary2[1][1] and Speed > 5 and prev_perf < 3):
        return 3,flag
    if(flag and Boundary3[0][0] <= x <= Boundary3[0][1] and Boundary3[1][0] <= y <= Boundary3[1][1] and Speed > 5 and prev_perf < 4):
        return 4,flag
    if(flag and Boundary4[0][0] <= x <= Boundary4[0][1] and Boundary4[1][0] <= y <= Boundary4[1][1] and Speed > 5 and prev_perf < 5):
        flag = False
        return 5,flag
    return prev_perf,flag 

# Helper function to get the pedstranian sign performance with moving Down. 
def PedstranianSignDown(stopPlace, flag, x, y, Speed, prev_perf):
    place = stopPlace[0][0]
    Boundary1 = [[place-13, place-3], [stopPlace[1][0], stopPlace[1][1]]]
    Boundary2 = [[place-23, place-13], [stopPlace[1][0], stopPlace[1][1]]]
    Boundary3 = [[place-33, place-23], [stopPlace[1][0], stopPlace[1][1]]]
    Boundary4 = [[place-100, place-33], [stopPlace[1][0], stopPlace[1][1]]]
    if(stopPlace[0][0] <= x <= stopPlace[0][1] and stopPlace[1][0] <= y <= stopPlace[1][1]):
        flag = True
    if(flag and Speed<=5):
        flag = False
        return prev_perf,flag
    if(flag and Boundary1[0][0] <= x <= Boundary1[0][1] and Boundary1[1][0] <= y <= Boundary1[1][1] and Speed>5 and prev_perf<2):
        return 2,flag    
    if(flag and Boundary2[0][0] <= x <= Boundary2[0][1] and Boundary2[1][0] <= y <= Boundary2[1][1] and Speed > 5 and prev_perf < 3):
        return 3,flag
    if(flag and Boundary3[0][0] <= x <= Boundary3[0][1] and Boundary3[1][0] <= y <= Boundary3[1][1] and Speed > 5 and prev_perf < 4):
        return 4,flag
    if(flag and Boundary4[0][0] <= x <= Boundary4[0][1] and Boundary4[1][0] <= y <= Boundary4[1][1] and Speed > 5 and prev_perf < 5):
        flag = False
        return 5,flag
    return prev_perf,flag

# Helper function to get the pedstranian sign performance with moving Up. 
def PedstranianSignUp(stopPlace, flag, x, y, Speed, prev_perf):
    place = stopPlace[0][0]
    Boundary1 = [[place+3, place+13], [stopPlace[1][0], stopPlace[1][1]]]
    Boundary2 = [[place+13, place+23], [stopPlace[1][0], stopPlace[1][1]]]
    Boundary3 = [[place+23, place+33], [stopPlace[1][0], stopPlace[1][1]]]
    Boundary4 = [[place+33, place+100], [stopPlace[1][0], stopPlace[1][1]]]
    if(stopPlace[0][0] <= x <= stopPlace[0][1] and stopPlace[1][0] <= y <= stopPlace[1][1]):
        flag = True
    if(flag and Speed<=5):
        flag = False
        return prev_perf,flag    
    if(flag and Boundary1[0][0] <= x <= Boundary1[0][1] and Boundary1[1][0] <= y <= Boundary1[1][1] and Speed>5 and prev_perf<2):
        return 2,flag    
    if(flag and Boundary2[0][0] <= x <= Boundary2[0][1] and Boundary2[1][0] <= y <= Boundary2[1][1] and Speed > 5 and prev_perf < 3):
        return 3,flag
    if(flag and Boundary3[0][0] <= x <= Boundary3[0][1] and Boundary3[1][0] <= y <= Boundary3[1][1] and Speed > 5 and prev_perf < 4):
        return 4,flag
    if(flag and Boundary4[0][0] <= x <= Boundary4[0][1] and Boundary4[1][0] <= y <= Boundary4[1][1] and Speed > 5 and prev_perf < 5):
        flag = False
        return 5,flag
    return prev_perf,flag