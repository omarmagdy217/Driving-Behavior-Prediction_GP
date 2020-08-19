import pickle
import numpy as np
import pickle
import subprocess
import csv
import time
import pandas as pd
import numpy as np
import SomeFns
import threading

filename = 'rank1_model.sav'
models = [pickle.load(open('rank1_model.sav', 'rb')), pickle.load(open('rank2_model.sav', 'rb')), pickle.load(open('rank3_model.sav', 'rb'))]
pca_reload = [pickle.load(open("pca1.pkl", 'rb')), pickle.load(open("pca2.pkl", 'rb')), pickle.load(open("pca3.pkl", 'rb'))]
scaler_reload = [pickle.load(open('scaler1.sav', 'rb')), pickle.load(open('scaler2.sav', 'rb')), pickle.load(open('scaler3.sav', 'rb'))]
print("Machine learning model loaded")
print("Result Can be viewed in Results_out")

def predict_mine(data_sample_list):
    global models
    global pca_reload
    global scaler_reload
    perf_values = [None] * 6
    # Make predictions. Store them in the variable y_pred.
    print("The array of data before machine learning processing\n")
    print(data_sample_list, flush=True)
    data_log_transformed = list(map(lambda x: np.log(x + 1), data_sample_list))
    # rank 1
    data_log_minmax = scaler_reload[0].transform([data_log_transformed])
    data_sample_pca = pca_reload[0].transform(data_log_minmax)
    #print(data_sample_pca.shape)
    y_pred = models[0].predict(data_sample_pca)
    perf_values[2], perf_values[5] = [np.asscalar(y_pred.round(2))] * 2
    # rank 2
    data_log_minmax = scaler_reload[1].transform([data_log_transformed])
    data_sample_pca = pca_reload[1].transform(data_log_minmax)
    #print(data_sample_pca.shape)
    y_pred = models[1].predict(data_sample_pca)
    perf_values[0], perf_values[3], perf_values[4] = [np.asscalar(y_pred.round(2))] * 3
    # rank 3
    data_log_minmax = scaler_reload[2].transform([data_log_transformed])
    data_sample_pca = pca_reload[2].transform(data_log_minmax)
    #print(data_sample_pca.shape)
    y_pred = models[2].predict(data_sample_pca)
    perf_values[1] = np.asscalar(y_pred.round(2))
    
    return perf_values


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

def Generate_Data(name="DataRecorded"):
    data = np.array([[]])
    global num_of_records
    for file_number in range(1, 31):
        name_of_file_to_read = "..\\Final_Data_recorded" + '\\' + name + str(num_of_records) + '.csv'
        num_of_records = num_of_records + 1
        loadData = pd.read_csv(name_of_file_to_read)
        temp_data = np.array(loadData)
        if (file_number == 1):
            data = temp_data
        else:
            data = np.concatenate((data, temp_data), axis=0)
    first_data_sample = Get_data_Sample_from_region(data)
    return first_data_sample

def pass_values_to_omar():
    data_sample = Generate_Data()
    array = predict_mine(data_sample[:-1])
    print("Output:", predict_mine(data_sample[:-1]))
    return array
