import matplotlib.pyplot as plt
import seaborn as sns
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from scipy.io import loadmat
import numpy as np
import SomeFns
import csv

f= open("output.txt","w+")

sf = 128

data_sample=["delta","theta","alpha","beta","gamma","state"]
with open('dataset_new.csv', 'w') as csvFile:
    weiter = csv.writer(csvFile)
    weiter.writerow(data_sample)
csvFile.close()


for dirname, _, filenames in os.walk('EEG DATA CSV after filtering'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        f.write(os.path.join(dirname, filename))
        f.write('\n')
        loadData = pd.read_csv(os.path.join(dirname, filename))
        data = np.array(loadData)

        for part in range(0, 3):
            ED_O2 = data[:, 1]
            segment = int(len(ED_O2) / 3)
            segment_of_segment = int(segment / 3)
            each_part = int(segment_of_segment /3)

            delta_1 = 0
            theta_1 = 0
            alpha_1 = 0
            beta_1 = 0
            gamma_1 = 0
            delta_2 = 0
            theta_2 = 0
            alpha_2 = 0
            beta_2 = 0
            gamma_2 = 0
            delta_3 = 0
            theta_3 = 0
            alpha_3 = 0
            beta_3 = 0
            gamma_3 = 0

            for part_data in range(0, 3):

                for i in range(0, 14):
                    if (part == 0):
                        ED_O2 = data[(segment_of_segment): (segment_of_segment * 2), i]
                        if (part_data == 0):
                            ED_O2 = ED_O2[0:each_part]
                        elif (part_data == 1):
                            ED_O2 = ED_O2[each_part:each_part*2]
                        elif (part_data == 2):
                            ED_O2 = ED_O2[each_part*2:each_part*3]

                    elif (part == 1):
                        ED_O2 = data[(segment_of_segment + segment): (segment_of_segment * 2 + segment), i]
                        if (part_data == 0):
                            ED_O2 = ED_O2[0:each_part]
                        elif (part_data == 1):
                            ED_O2 = ED_O2[each_part:each_part*2]
                        elif (part_data == 2):
                            ED_O2 = ED_O2[each_part*2:each_part*3]

                    elif(part==2):
                        ED_O2 = data[ ( 2*segment+segment_of_segment ): ( 2*segment + segment_of_segment * 2 ), i]
                        if (part_data ==0 ):
                            ED_O2 = ED_O2[0:each_part]
                        elif (part_data == 1):
                            ED_O2 = ED_O2[each_part:each_part*2]
                        elif (part_data == 2):
                            ED_O2 = ED_O2[each_part*2:each_part*3]
                # Define the duration of the window to be 4 seconds
                win_sec = 4

                # Compute average absolute power of Delta band
                delta_power = SomeFns.bandpower(ED_O2, sf, [0.5, 4], win_sec)

                # Compute average absolute power of Theta band
                theta_power = SomeFns.bandpower(ED_O2, sf, [4, 8], win_sec)

                # Compute average absolute power of Alpha band
                alpha_power = SomeFns.bandpower(ED_O2, sf, [8, 12], win_sec)

                # Compute average absolute power of Beta band
                beta_power = SomeFns.bandpower(ED_O2, sf, [12, 30], win_sec)

                # Compute average absolute power of Gamma band
                gamma_power = SomeFns.bandpower(ED_O2, sf, [30, 100], win_sec)

                if (part_data == 0):
                    delta_1 = delta_1 + delta_power
                    theta_1 = theta_1 + theta_power
                    alpha_1 = alpha_1 + alpha_power
                    beta_1 = beta_1 + beta_power
                    gamma_1 = gamma_1 + gamma_power
                elif (part_data == 1):
                    delta_2 = delta_2 + delta_power
                    theta_2 = theta_2 + theta_power
                    alpha_2 = alpha_2 + alpha_power
                    beta_2 = beta_2 + beta_power
                    gamma_2 = gamma_2 + gamma_power
                elif (part_data == 2):
                    delta_3 = delta_3 + delta_power
                    theta_3 = theta_3 + theta_power
                    alpha_3 = alpha_3 + alpha_power
                    beta_3 = beta_3 + beta_power
                    gamma_3 = gamma_3 + gamma_power

            data_sample = [delta_1, theta_1, alpha_1, beta_1, gamma_1, 1]

            with open('dataset_new.csv', 'a') as csvFile:
                weiter = csv.writer(csvFile)
                weiter.writerow(data_sample)
            csvFile.close()

            data_sample = [delta_2, theta_2, alpha_2, beta_2, gamma_2, 2]

            with open('dataset_new.csv', 'a') as csvFile:
                weiter = csv.writer(csvFile)
                weiter.writerow(data_sample)
            csvFile.close()

            data_sample = [delta_3, theta_3, alpha_3, beta_3, gamma_3, 3]

            with open('dataset_new.csv', 'a') as csvFile:
                weiter = csv.writer(csvFile)
                weiter.writerow(data_sample)
            csvFile.close()