import subprocess
import csv
import time

process = ""

def Open_new_file(name):
    first_row = [ 'SampleNumber', 'number of' ,'AF3', 'F7', 'F3', 'FC5', 'T7', 'P7', 'O1', 'O2','P8' ,'T8' ,'FC6', 'F4', 'F8', 'AF4',
                 "Zeros", "Zeros_brdo"]
    name_of_the_file = name + '.csv'

    with open(name + '.csv', 'w+') as csvFile:
        w = csv.writer(csvFile)
        w.writerow(first_row)
    csvFile.close()

    return name_of_the_file

def Data_Recoder1(sec):
    name_of_the_file=""
    time.sleep(5)
    process = subprocess.Popen("cd HeadSet\Py3&&python.exe CyKIT.py 127.0.0.1 54123 6 outputdata+noweb",
                                    shell=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for index in range(9):
        line = process.stdout.readline()

    file_counter = 1
    while file_counter<sec:
        index = 0
        name = "Data_recorded\DataRecorded" + str(file_counter)
        name_of_the_file=Open_new_file(name)
        log_file = open("Recording_Logs.txt", "a")
        with open(name_of_the_file, 'a') as csvFile:
            start = time.time()
            while index < 128:
                index = index + 1
                line = process.stdout.readline()
                line = line[:-2]
                line = str(line)
                #print(line)
                data = line.split(",")  # split string into a list
                data[0] = data[0][2:]
                data[17] = data[17][:-1]

                w = csv.writer(csvFile)
                w.writerow(data)
            end = time.time()
            log_file.write("Recording now ===>> " + name_of_the_file + " with time = "+str(end - start)+"\n")
        csvFile.close()
        log_file.close()
        file_counter = file_counter + 1


def Data_Recoder2():
    name_of_the_file=""
    global process
    process = subprocess.Popen("cd HeadSet\Py3&&python.exe CyKIT.py 127.0.0.1 54123 6 outputdata+noweb",
                                    shell=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for index in range(9):
        line = process.stdout.readline()

    file_counter = 1
    #while file_counter<sec*128:
    while 1:
        index = 0
        name = "Data_recorded2\DataRecorded" + str(file_counter)
        name_of_the_file=Open_new_file(name)
        log_file = open("Recording_Logs.txt", "a")
        with open(name_of_the_file, 'a') as csvFile:
            start = time.time()
            while index < 128:
                index = index + 1
                try:
                    line = process.stdout.readline()
                except:
                    return
                line = line[:-2]
                line = str(line)
                #print(line)
                data = line.split(",")  # split string into a list
                data[0] = data[0][2:]
                data[17] = data[17][:-1]

                w = csv.writer(csvFile)
                w.writerow(data)
            end = time.time()
            log_file.write("Recording now ===>> " + name_of_the_file + " with time = "+str(end - start)+"\n")
        csvFile.close()
        log_file.close()
        file_counter = file_counter + 1

def Stop_Data_Recoder2():
    global process
    process.kill()


"""
def main():
    Data_Recoder1()


if __name__ == "__main__":
    main() 
"""