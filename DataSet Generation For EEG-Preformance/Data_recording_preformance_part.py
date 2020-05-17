import os
import threading
import Record_Data
import Processing_Recorded_data
import time
import subprocess

def get_score():
    with open("Output.txt", "r") as file:
        first_line = file.readline()
        for last_line in file:
            pass
    score = first_line.rstrip('\n')
    print("\n" + score)
    return int(score)

def get_preformance():
    os.system('python.exe Calculate_preformance/main.py')

def Start_one_iteration():
    print("We are recording now Please wait")
    #30 is the number of sec that we will record
    Record_Data.Data_Recoder1(30)
    print("Start playing after 10 secs \n Don't forget to press R to start record please :)")
    #time.sleep(60)
    print("Please press any thing in terminal after finishing the track\n Don't forget to press R to stops please :)")
    #Record_Data.Data_Recoder2()
    input()
    #Record_Data.Stop_Data_Recoder2()
    get_preformance()
    final_score=get_score()
    Processing_Recorded_data.Data_Generator(final_score)

def our_loop():
    while True:
        print("Are You Ready to start???")
        input()
        Start_one_iteration()



def runSimulator():
    # Run the "Blocks" environment located at ./Blocks/Blocks.exe
    #os.system('"' + os.getcwd() + "/SoundTrackApplication/WindowsNoEditor/MyProject.exe" + '"')
    os.system('"' + os.getcwd() + "/rank1/RankRoads.exe" + '"')

def main():
    # Create a new thread for running the simulator
    simulatorThread = threading.Thread(target=runSimulator)

    # Start the simulator thread
    simulatorThread.start()

    our_loop()






if __name__ == "__main__":
    main()