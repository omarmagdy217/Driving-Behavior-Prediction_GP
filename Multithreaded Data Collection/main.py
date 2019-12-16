import os
import threading


def runSimulator():
    # Run the "Blocks" environment located at ./Blocks/Blocks.exe
    os.system(os.getcwd() + "/Blocks/Blocks.exe")


def main():
    # Create a new thread for running the simulator
    simulatorThread = threading.Thread(target=runSimulator)

    # Start the simulator thread
    simulatorThread.start()


if __name__ == "__main__":
    main()
