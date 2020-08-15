
import os.path as path
import time
import math
import rank1_road1l as road2 
import rank1_road1r as road1
import rank1_road2l as road4
import rank1_road2r as road3
import rank1_road3l as road6
import rank1_road3r as road5
import rank1_road4l as road7
import rank1_road4r as road8

import rank2_road1r as road2_1
import rank2_road1l as road2_2
import rank2_road2r as road2_3
import rank2_road2l as road2_4
import rank2_road3r as road2_5
import rank2_road3l as road2_6
import rank2_road4r as road2_7
import rank2_road4l as road2_8

import rank3_road1r as road3_1
import rank3_road1l as road3_2
import rank3_road2r as road3_3
import rank3_road2l as road3_4
import rank3_road3r as road3_5
import rank3_road3l as road3_6
import rank3_road4r as road3_7
import rank3_road4l as road3_8

log_path = path.expanduser('~\\Documents\\AirSim\\airsim_rec.txt')

f= open("RankRoads\\road.txt","r")
inp = f.read()
rank = int(inp[0])
roadNum = int(inp[3])

if(rank == 1):
    if(roadNum==1):
        p,CP = road1.analyse(log_path)
        outfile = open("Rank1Road1ROutput.txt","w+")
        outfile.write("RANK: 1\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")

    elif(roadNum==2):
        p,CP = road2.analyse(log_path)
        outfile = open("Rank1Road1LOutput.txt","w+")
        outfile.write("RANK: 1\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")        

    elif(roadNum==3):
        p,CP = road3.analyse(log_path)
        outfile = open("Rank1Road2ROutput.txt","w+")
        outfile.write("RANK: 1\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")        

    elif(roadNum==4):
        p,CP = road4.analyse(log_path)
        outfile = open("Rank1Road2LOutput.txt","w+")
        outfile.write("RANK: 1\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n") 

    elif(roadNum==5):
        p,CP = road5.analyse(log_path)
        outfile = open("Rank1Road3ROutput.txt","w+")
        outfile.write("RANK: 1\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n") 

    elif(roadNum==6):
        p,CP = road6.analyse(log_path)
        outfile = open("Rank1Road3LOutput.txt","w+")
        outfile.write("RANK: 1\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")         

    elif(roadNum==7):
        p,CP = road7.analyse(log_path)
        outfile = open("Rank1Road4LOutput.txt","w+")
        outfile.write("RANK: 1\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")         

    elif(roadNum==8):
        p,CP = road8.analyse(log_path)
        outfile = open("Rank1Road4ROutput.txt","w+")
        outfile.write("RANK: 1\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")        
elif(rank == 2):
    if(roadNum == 1):
        p,CP = road2_1.analyse(log_path)
        outfile = open("Rank2Road1ROutput.txt","w+")
        outfile.write("RANK: 2\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")            

    elif(roadNum == 2):
        p,CP = road2_2.analyse(log_path)
        outfile = open("Rank2Road1LOutput.txt","w+")
        outfile.write("RANK: 2\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")    
    
    elif(roadNum == 3):
        p,CP = road2_3.analyse(log_path)
        outfile = open("Rank2Road2ROutput.txt","w+")
        outfile.write("RANK: 2\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")   
    
    elif(roadNum == 4):
        p,CP = road2_4.analyse(log_path)
        outfile = open("Rank2Road2LOutput.txt","w+")
        outfile.write("RANK: 2\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")   

    elif(roadNum == 5):
        p,CP = road2_5.analyse(log_path)
        outfile = open("Rank2Road3ROutput.txt","w+")
        outfile.write("RANK: 2\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")   
    
    elif(roadNum == 6):
        p,CP = road2_6.analyse(log_path)
        outfile = open("Rank2Road3LOutput.txt","w+")
        outfile.write("RANK: 2\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")           

    elif(roadNum == 7):
        p,CP = road2_7.analyse(log_path)
        outfile = open("Rank2Road4ROutput.txt","w+")
        outfile.write("RANK: 2\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")   
    
    elif(roadNum == 8):
        p,CP = road2_8.analyse(log_path)
        outfile = open("Rank2Road4LOutput.txt","w+")
        outfile.write("RANK: 2\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")  

elif(rank == 3):
    if(roadNum == 1):
        p,CP = road3_1.analyse(log_path)
        outfile = open("Rank3Road1ROutput.txt","w+")
        outfile.write("RANK: 3\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")            

    elif(roadNum == 2):
        p,CP = road3_2.analyse(log_path)
        outfile = open("Rank3Road1LOutput.txt","w+")
        outfile.write("RANK: 3\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")    
    
    elif(roadNum == 3):
        p,CP = road3_3.analyse(log_path)
        outfile = open("Rank3Road2ROutput.txt","w+")
        outfile.write("RANK: 3\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")   
    
    elif(roadNum == 4):
        p,CP = road3_4.analyse(log_path)
        outfile = open("Rank3Road2LOutput.txt","w+")
        outfile.write("RANK: 3\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")   

    elif(roadNum == 5):
        p,CP = road3_5.analyse(log_path)
        outfile = open("Rank3Road3ROutput.txt","w+")
        outfile.write("RANK: 3\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")   
    
    elif(roadNum == 6):
        p,CP = road3_6.analyse(log_path)
        outfile = open("Rank3Road3LOutput.txt","w+")
        outfile.write("RANK: 3\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")           

    elif(roadNum == 7):
        p,CP = road3_7.analyse(log_path)
        outfile = open("Rank3Road4ROutput.txt","w+")
        outfile.write("RANK: 3\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")   
    
    elif(roadNum == 8):
        p,CP = road3_8.analyse(log_path)
        outfile = open("Rank3Road4LOutput.txt","w+")
        outfile.write("RANK: 3\n")
        outfile.write("OVERALL PERFORMANCE: " + str(math.ceil(100-((p-1)/4)*100)) + "%\n")
        outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
        for i in CP:
            outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")  



