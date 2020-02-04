import os
import threading
import Record_Data

def runSimulator():
    # Run the "Blocks" environment located at ./Blocks/Blocks.exe
    #os.system('"' + os.getcwd() + "/SoundTrackApplication/WindowsNoEditor/MyProject.exe" + '"')
    os.system('"' + os.getcwd() + "/WindowsNoEditor/MRT.exe" + '"')

def main():
    # Create a new thread for running the simulator
    simulatorThread = threading.Thread(target=runSimulator)

    # Start the simulator thread
    simulatorThread.start()

    #Run the headset from the main thread
    Record_Data.Data_Recoder()



if __name__ == "__main__":
    main()