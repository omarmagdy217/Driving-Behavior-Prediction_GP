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

log_path = path.expanduser('~\\Documents\\AirSim\\airsim_rec.txt')

f= open("Rank1\\RankRoads\\road.txt","r")
roadNum = int(f.read())
print(roadNum)

if(roadNum==1):
    p,CP = road1.analyse(log_path)
    outfile = open("Output.txt","w+")
    #outfile.write("RANK: 1\n")
    #outfile.write("OVERALL PERFORMANCE: " + str(100-(p/5)*100) + "%\n")
    outfile.write(str(100 - (p / 5) * 100))
    outfile.write("\n")
    outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
    for i in CP:
        outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")

elif(roadNum==2):
    p,CP = road2.analyse(log_path)
    outfile = open("Output.txt","w+")
    #outfile.write("RANK: 1\n")
    #outfile.write("OVERALL PERFORMANCE: " + str(100-(p/5)*100) + "%\n")
    outfile.write(str(100 - (p / 5) * 100))
    outfile.write("\n")
    outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
    for i in CP:
        outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")        

elif(roadNum==3):
    p,CP = road3.analyse(log_path)
    outfile = open("Output.txt","w+")
    #outfile.write("RANK: 1\n")
    #outfile.write("OVERALL PERFORMANCE: " + str(100-(p/5)*100) + "%\n")
    outfile.write(str(100 - (p / 5) * 100))
    outfile.write("\n")
    outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
    for i in CP:
        outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")        

elif(roadNum==4):
    p,CP = road4.analyse(log_path)
    outfile = open("Output.txt","w+")
    #outfile.write("RANK: 1\n")
    #outfile.write("OVERALL PERFORMANCE: " + str(100-(p/5)*100) + "%\n")
    outfile.write(str(100 - (p / 5) * 100))
    outfile.write("\n")
    outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
    for i in CP:
        outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n") 

elif(roadNum==5):
    p,CP = road5.analyse(log_path)
    outfile = open("Output.txt","w+")
    #outfile.write("RANK: 1\n")
    #outfile.write("OVERALL PERFORMANCE: " + str(100-(p/5)*100) + "%\n")
    outfile.write(str(100 - (p / 5) * 100))
    outfile.write("\n")
    outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
    for i in CP:
        outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n") 

elif(roadNum==6):
    p,CP = road6.analyse(log_path)
    outfile = open("Output.txt","w+")
    #outfile.write("RANK: 1\n")
    #outfile.write("OVERALL PERFORMANCE: " + str(100-(p/5)*100) + "%\n")
    outfile.write(str(100 - (p / 5) * 100))
    outfile.write("\n")
    outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
    for i in CP:
        outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")         

elif(roadNum==8):
    p,CP = road7.analyse(log_path)
    outfile = open("Output.txt","w+")
    #outfile.write("RANK: 1\n")
    #outfile.write("OVERALL PERFORMANCE: " + str(100-(p/5)*100) + "%\n")
    outfile.write(str(100 - (p / 5) * 100))
    outfile.write("\n")
    outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
    for i in CP:
        outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")         

elif(roadNum==7):
    p,CP = road8.analyse(log_path)
    outfile = open("Output.txt","w+")
    #outfile.write("RANK: 1\n")
    #outfile.write("OVERALL PERFORMANCE: " + str(100-(p/5)*100) + "%\n")
    outfile.write(str(100 - (p / 5) * 100))
    outfile.write("\n")
    outfile.write("EPOCH TIMESTAMP(Every ~1000 ms)      Performance( Scale: 1-5)\n")
    for i in CP:
        outfile.write(str(i[0]) + "                        " + str(i[1]) + "\n")