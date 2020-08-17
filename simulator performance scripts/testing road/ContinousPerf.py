# Helper function to get the continous performance with moving upward or downward in right lane. 
def MovVerticalRightLane(roadDims,x,y):
    half = roadDims[1][0] + abs(roadDims[1][0]-roadDims[1][1])/2
    Boundary1 = [[roadDims[0][0],roadDims[0][1]],[half,roadDims[1][1]]]
    Boundary2 = [[roadDims[0][0],roadDims[0][1]],[half-1,half]]
    Boundary3 = [[roadDims[0][0],roadDims[0][1]],[half-2,half-1]]
    Boundary4 = [[roadDims[0][0],roadDims[0][1]],[half-3,half-2]]
    Boundary5 = [[roadDims[0][0],roadDims[0][1]],[half-10,half-3]]
    if(Boundary1[0][0] <= x <= Boundary1[0][1] and Boundary1[1][0] <= y <= Boundary1[1][1]):
        return 1
    if(Boundary2[0][0] <= x <= Boundary2[0][1] and Boundary2[1][0] <= y <= Boundary2[1][1]):
        return 2
    if(Boundary3[0][0] <= x <= Boundary3[0][1] and Boundary3[1][0] <= y <= Boundary3[1][1]):
        return 3
    if(Boundary4[0][0] <= x <= Boundary4[0][1] and Boundary4[1][0] <= y <= Boundary4[1][1]):
        return 4
    if(Boundary5[0][0] <= x <= Boundary5[0][1] and Boundary5[1][0] <= y <= Boundary5[1][1]):
        return 5
    return 0

        

# Helper function to get the continous performance with moving leftward or rightward in up lane. 
def MovHorizontalupLane(roadDims,x,y):
    half = roadDims[0][0] + abs(roadDims[0][0]-roadDims[0][1])/2
    Boundary1 = [[half,roadDims[0][1]],[roadDims[1][0],roadDims[1][1]]]
    Boundary2 = [[half-1,half],[roadDims[1][0],roadDims[1][1]]]
    Boundary3 = [[half-2,half-1],[roadDims[1][0],roadDims[1][1]]]
    Boundary4 = [[half-3,half-2],[roadDims[1][0],roadDims[1][1]]]
    Boundary5 = [[half-10,half-3],[roadDims[1][0],roadDims[1][1]]]
    if(Boundary1[0][0] <= x <= Boundary1[0][1] and Boundary1[1][0] <= y <= Boundary1[1][1]):
        return 1
    if(Boundary2[0][0] <= x <= Boundary2[0][1] and Boundary2[1][0] <= y <= Boundary2[1][1]):
        return 2
    if(Boundary3[0][0] <= x <= Boundary3[0][1] and Boundary3[1][0] <= y <= Boundary3[1][1]):
        return 3
    if(Boundary4[0][0] <= x <= Boundary4[0][1] and Boundary4[1][0] <= y <= Boundary4[1][1]):
        return 4
    if(Boundary5[0][0] <= x <= Boundary5[0][1] and Boundary5[1][0] <= y <= Boundary5[1][1]):
        return 5
    return 0				



# Helper function to get the continous performance with moving upward or downward in left lane.  
def MovVerticalLeftLane(roadDims,x,y):
    half = roadDims[1][0] + abs(roadDims[1][0]-roadDims[1][1])/2
    Boundary1 = [[roadDims[0][0],roadDims[0][1]],[roadDims[1][0],half]]
    Boundary2 = [[roadDims[0][0],roadDims[0][1]],[half,half+1]]
    Boundary3 = [[roadDims[0][0],roadDims[0][1]],[half+1,half+2]]
    Boundary4 = [[roadDims[0][0],roadDims[0][1]],[half+2,half+3]]
    Boundary5 = [[roadDims[0][0],roadDims[0][1]],[half+3,half+10]]
    if(Boundary1[0][0] <= x <= Boundary1[0][1] and Boundary1[1][0] <= y <= Boundary1[1][1]):
        return 1
    if(Boundary2[0][0] <= x <= Boundary2[0][1] and Boundary2[1][0] <= y <= Boundary2[1][1]):
        return 2
    if(Boundary3[0][0] <= x <= Boundary3[0][1] and Boundary3[1][0] <= y <= Boundary3[1][1]):
        return 3
    if(Boundary4[0][0] <= x <= Boundary4[0][1] and Boundary4[1][0] <= y <= Boundary4[1][1]):
        return 4
    if(Boundary5[0][0] <= x <= Boundary5[0][1] and Boundary5[1][0] <= y <= Boundary5[1][1]):
        return 5
    return 0



# Helper function to get the continous performance with moving leftward or rightward in down lane. 
def MovHorizontalDownLane(roadDims,x,y):
    half = roadDims[0][0] + abs(roadDims[0][0]-roadDims[0][1])/2
    Boundary1 = [[roadDims[0][0],half],[roadDims[1][0],roadDims[1][1]]]
    Boundary2 = [[half,half+1],[roadDims[1][0],roadDims[1][1]]]
    Boundary3 = [[half+1,half+2],[roadDims[1][0],roadDims[1][1]]]
    Boundary4 = [[half+2,half+3],[roadDims[1][0],roadDims[1][1]]]
    Boundary5 = [[half+3,half+10],[roadDims[1][0],roadDims[1][1]]]
    if(Boundary1[0][0] <= x <= Boundary1[0][1] and Boundary1[1][0] <= y <= Boundary1[1][1]):
        return 1
    if(Boundary2[0][0] <= x <= Boundary2[0][1] and Boundary2[1][0] <= y <= Boundary2[1][1]):
        return 2
    if(Boundary3[0][0] <= x <= Boundary3[0][1] and Boundary3[1][0] <= y <= Boundary3[1][1]):
        return 3
    if(Boundary4[0][0] <= x <= Boundary4[0][1] and Boundary4[1][0] <= y <= Boundary4[1][1]):
        return 4
    if(Boundary5[0][0] <= x <= Boundary5[0][1] and Boundary5[1][0] <= y <= Boundary5[1][1]):
        return 5
    return 0