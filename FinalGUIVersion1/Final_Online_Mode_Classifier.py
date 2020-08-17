import pickle
import subprocess
import csv
import time
import pandas as pd
import numpy as np
import SomeFns
import threading
import os
from sklearn.preprocessing import MinMaxScaler

#######################################################################
######### 5aly balak al file mazboot 3ala Mode each 30 sec  ###########
#######################################################################
My_State=""
ok = True
num_of_records=1;
filename = 'Final_Mental_State_ML_Model/finalized_model.sav'
states_class = ['Focused', 'De-Focused', 'Drowsy']
model = pickle.load(open(filename, 'rb'))
pca_reload = pickle.load(open("Final_Mental_State_ML_Model/pca.pkl", 'rb'))
scaler_reload = pickle.load(open('Final_Mental_State_ML_Model/scaler.sav', 'rb'))
print("Machine learning model loaded")
print("Result Can be viewed in Results_out")

def predict_mine(data_sample_list):
    global model
    global My_State
    global states_class
    global num_of_records
    print("The array of data before machine learning processing\n")
    print(data_sample_list, flush=True)
    data_log_transformed = list(map(lambda x: np.log(x + 1), data_sample_list))
    data_log_minmax = scaler_reload.transform([data_log_transformed])
    data_sample_pca = pca_reload.transform(data_log_minmax)
    print(data_sample_pca.shape)
    y_pred = model.predict(data_sample_pca)
    # Label states class.
    states_class = ['Focused', 'De-Focused', 'Drowsy']
    for i, state in enumerate(y_pred):
        log_file = open("Results_out" + ".txt", "a+")
        print("Predicted mental state from sec {} to {} sec : {}".format(num_of_records - 30, num_of_records ,states_class[int(state - 1)]))
        log_file.write("Predicted mental state from sec {} to {} sec : {}\n".format(num_of_records - 30, num_of_records ,states_class[int(state - 1)]))
        log_file.close()
        My_State = states_class[int(state - 1)]

def Online_test():
    data_sample=Generate_Data()
    predict_mine(data_sample[:-1])

def Generate_Data(name="DataRecorded"):
    data = np.array([[]])
    global num_of_records
    for file_number in range(1, 31):
        """
            This loop just get data from 30 second 
        """
        name_of_file_to_read = "Final_Online_Mental_Data_recorded" + '\\' + name + str(num_of_records) + '.csv'
        num_of_records = num_of_records + 1
        loadData = pd.read_csv(name_of_file_to_read)
        temp_data = np.array(loadData)
        if (file_number == 1):
            data = temp_data
        else:
            data = np.concatenate((data, temp_data), axis=0)
    first_data_sample = Get_data_Sample_from_region(data)
    return first_data_sample

def Get_data_Sample_from_region(data):
    """
        This function just take the region of the datasample and it loop on all the channels to calculate the
        avg power from all of them
    """
    data_sample = [0, 0, 0, 0, 0]
    """
        Use this line if you want to take all channels
        #for channel in range(0, self.num_of_channels):
    """
    new_data_sample = []
    selective_channels = [1,2, 3,4,5, 6, 7, 8, 9,10,11,12,13, 14]
    sf = 128
    num_of_channels = 14
    for channel in selective_channels:
        """
            if data is filtered:
            data_part=data[region[0]:region[1],channel-1]
        """
        data_part = data[:, channel + 1]
        # Define the duration of the window to be 4 seconds
        win_sec = 4
        # Compute average absolute power of Delta band
        delta_power = SomeFns.bandpower(data_part, sf, [0.5, 4], win_sec)
        data_sample[0] += delta_power
        new_data_sample.append(delta_power)
        # Compute average absolute power of Theta band
        theta_power = SomeFns.bandpower(data_part, sf, [4, 8], win_sec)
        data_sample[1] += theta_power
        new_data_sample.append(theta_power)
        # Compute average absolute power of Alpha band
        alpha_power = SomeFns.bandpower(data_part, sf, [8, 12], win_sec)
        data_sample[2] += alpha_power
        new_data_sample.append(alpha_power)
        # Compute average absolute power of Beta band
        beta_power = SomeFns.bandpower(data_part, sf, [12, 30], win_sec)
        data_sample[3] += beta_power
        new_data_sample.append(beta_power)
        # Compute average absolute power of Gamma band
        gamma_power = SomeFns.bandpower(data_part, sf, [30, 100], win_sec)
        data_sample[4] += gamma_power
        new_data_sample.append(gamma_power)
    for feature in range(0, 5):
        data_sample[feature] = data_sample[feature] / num_of_channels
    """
        if you want the old approach of 5 numbers per each datasample use this line
        #return data_sample
    """
    new_data_sample.append(0)
    return new_data_sample

def Open_new_file(name):
    first_row = [ 'SampleNumber', 'number of' ,'AF3', 'F7', 'F3', 'FC5', 'T7', 'P7', 'O1', 'O2','P8' ,'T8' ,'FC6', 'F4', 'F8', 'AF4',
                 "Zeros", "Zeros_brdo"]
    name_of_the_file = name + '.csv'

    with open(name + '.csv', 'w+') as csvFile:
        w = csv.writer(csvFile)
        w.writerow(first_row)
    csvFile.close()

    return name_of_the_file

def Start_the_head_set_recording():
    process = subprocess.Popen("cd HeadSet\Py3&&python.exe CyKIT.py 127.0.0.1 54123 6 outputdata+noweb",
                               shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for index in range(9):
        line = process.stdout.readline()

    return process

def StartFromHere():
    global ok
    s=""
    process = Start_the_head_set_recording()
    file_counter = 1
    while ok:
        index = 0
        name = "Final_Online_Mental_Data_recorded\DataRecorded" + str(file_counter)
        name_of_the_file = Open_new_file(name)
        log_file = open("Recording_Logs.txt", "a")
        with open(name_of_the_file, 'a') as csvFile:
            start = time.time()
            while index < 128:
                index = index + 1
                line = process.stdout.readline()
                line = line[:-2]
                line = str(line)
                data = line.split(",")
                data[0] = data[0][2:]
                data[17] = data[17][:-1]
                w = csv.writer(csvFile)
                w.writerow(data)
            end = time.time()
        csvFile.close()
        file_counter = file_counter + 1
        if(file_counter%31==0):
            Thread4 = threading.Thread(target=Online_test)
            Thread4.start()
    process.terminate()
class refresher():
    state=""
    def updatez(self):
        global My_State
        return My_State
    def change(self):
        global ok
        ok=False