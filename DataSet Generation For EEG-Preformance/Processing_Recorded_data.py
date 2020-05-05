import pandas as pd
import numpy as np
import SomeFns
import csv

selective_channels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
num_of_channels= 14
sf=128
def Data_Generator(state):
    # must defined before run the script
    num_of_sec_per_data_sample = 30
    # ================================
    name_of_the_file = "data1.csv"
    source_of_data= "Data_recorded"
    num_of_records = 1
    name="DataRecorded"

    data=np.array([[]])
    for file_number in range(1, (num_of_sec_per_data_sample+1)):
        name_of_file_to_read=source_of_data+'\\'+name+str(num_of_records)+'.csv'
        num_of_records=num_of_records+1
        loadData = pd.read_csv( name_of_file_to_read )
        temp_data = np.array(loadData)
        if(file_number==1):
            data=temp_data
        else:
            data=np.concatenate((data,temp_data),axis=0)
        #self.Divide_Data_the_generate(data)
    print(np.size(data, 0))
    print(np.size(data, 1))
    first_data_sample = Get_data_Sample_from_region(data,state)
    with open(name_of_the_file, 'a') as csvFile:
        w = csv.writer(csvFile)
        w.writerow(first_data_sample)
    csvFile.close()

def Get_data_Sample_from_region(data, state):
    """
        This function just take the region of the datasample and it loop on all the channels to calculate the
        avg power from all of them
    """
    data_sample=[0,0,0,0,0,state]
    """
        Use this line if you want to take all channels
        #for channel in range(0, self.num_of_channels):
    """
    new_data_sample=[]
    for channel in selective_channels:
        """
            if data is filtered:
            data_part=data[region[0]:region[1],channel-1]
        """
        data_part=data[:,channel+1]
        # Define the duration of the window to be 4 seconds
        win_sec = 4
        # Compute average absolute power of Delta band
        delta_power = SomeFns.bandpower(data_part, sf, [0.5, 4], win_sec)
        data_sample[0]+=delta_power
        new_data_sample.append(delta_power)
        # Compute average absolute power of Theta band
        theta_power = SomeFns.bandpower(data_part, sf, [4, 8], win_sec)
        data_sample[1] +=theta_power
        new_data_sample.append(theta_power)
        # Compute average absolute power of Alpha band
        alpha_power = SomeFns.bandpower(data_part, sf, [8, 12], win_sec)
        data_sample[2] +=alpha_power
        new_data_sample.append(alpha_power)
        # Compute average absolute power of Beta band
        beta_power = SomeFns.bandpower(data_part, sf, [12, 30], win_sec)
        data_sample[3] +=beta_power
        new_data_sample.append(beta_power)
        # Compute average absolute power of Gamma band
        gamma_power = SomeFns.bandpower(data_part, sf, [30, 100], win_sec)
        data_sample[4] +=gamma_power
        new_data_sample.append(gamma_power)
    for feature in range(0, 5):
        data_sample[feature]=data_sample[feature]/num_of_channels
    """
        if you want the old approach of 5 numbers per each datasample use this line
        #return data_sample
    """
    new_data_sample.append(state)
    return new_data_sample

"""
def main():
    Data_Generator(2)

if __name__ == "__main__":
    main()
"""