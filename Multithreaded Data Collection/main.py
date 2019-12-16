import os
import threading


def runSimulator():
    os.system(os.getcwd() + "/Blocks/Blocks.exe")


def main():
    simulatorThread = threading.Thread(target=runSimulator)
    simulatorThread.start()


if __name__ == "__main__":
    main()
