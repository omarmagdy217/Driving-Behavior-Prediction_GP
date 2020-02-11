import pickle
import subprocess
import csv
import time
import pandas as pd
import numpy as np
import SomeFns
import threading

num_of_records=1;
filename = 'finalized_model.sav'
states_class = ['Focused', 'De-Focused', 'Drowsy']
model = pickle.load(open(filename, 'rb'))
pca_reload = pickle.load(open("pca.pkl", 'rb'))
print("Machine learning model loaded")
log_file=open("Results_out" + ".txt", "w+")
print("Result Can be viewed in Results_out")

def predict_mine(data_sample_list):
    global model
    global states_class
    global num_of_records
    # Make predictions. Store them in the variable y_pred.
    data_sample = np.array(data_sample_list)
    data_sample = np.reshape(data_sample, (1, data_sample.size))
    data_sample.reshape(71,1)
    print(data_sample.shape)
    data_sample_pca=pca_reload.transform(data_sample)
    print(data_sample_pca.shape)
    y_pred = model.predict(data_sample_pca)
    # Label states class.
    states_class = ['Focused', 'De-Focused', 'Drowsy']
    # Show predictions
    for i, state in enumerate(y_pred):
        print("Predicted mental state from sec {} to {} sec : {}".format(num_of_records - 30, num_of_records ,states_class[int(state - 1)]))
        log_file.write("Predicted mental state from sec {} to {} sec : {}\n".format(num_of_records - 30, num_of_records ,states_class[int(state - 1)]))
def Online_test():
    data_sample=Generate_Data()
    print(data_sample)
    predict_mine(data_sample)

def Generate_Data(name="DataRecorded"):
    data = np.array([[]])
    global num_of_records
    for file_number in range(1, 31):
        """
            This loop just get data from 30 second 
        """
        name_of_file_to_read = "Data_recorded" + '\\' + name + str(num_of_records) + '.csv'
        #print(name_of_file_to_read)
        num_of_records = num_of_records + 1
        loadData = pd.read_csv(name_of_file_to_read)
        temp_data = np.array(loadData)
        if (file_number == 1):
            data = temp_data
        else:
            data = np.concatenate((data, temp_data), axis=0)
        #self.Divide_Data_the_generate(data)
    #print(np.size(data, 0))
    #print(np.size(data, 1))
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

def main():
    input("Press Enter to Start Recording...")

    # Run the headset from the main thread
    process=Start_the_head_set_recording()
    file_counter = 1
    while True:
        index = 0
        name = "Data_recorded\DataRecorded" + str(file_counter)
        name_of_the_file = Open_new_file(name)
        log_file = open("Recording_Logs.txt", "a")
        with open(name_of_the_file, 'a') as csvFile:
            start = time.time()
            while index < 128:
                index = index + 1
                line = process.stdout.readline()
                line = line[:-2]
                line = str(line)
                # print(line)
                data = line.split(",")  # split string into a list
                data[0] = data[0][2:]
                data[17] = data[17][:-1]

                w = csv.writer(csvFile)
                w.writerow(data)
            end = time.time()
        csvFile.close()
        file_counter = file_counter + 1
        if(file_counter%31==0):
            # Create a new thread for online_testing
            new_Thread = threading.Thread(target=Online_test)
            # Start the simulator thread
            new_Thread.start()
    log_file.close()

if __name__ == "__main__":
    main()