import matplotlib.pyplot as plt
import seaborn as sns
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from scipy.io import loadmat
import numpy as np
import SomeFns
import csv

num_of_records=0
sf = 128

delta_1=0
theta_1 =0
alpha_1=0
beta_1  =0
gamma_1 =0
delta_2=0
theta_2 =0
alpha_2=0
beta_2 =0
gamma_2 =0
delta_3=0
theta_3 =0
alpha_3=0
beta_3  =0
gamma_3 =0

data_base=[]

f= open("output.txt","w+")

data_sample=["delta","theta","alpha","beta","gamma","state"]
with open('dataset.csv', 'w') as csvFile:
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

        for i in range(0,13):

            ED_O2 = data[:, i]
            segment=int(len(ED_O2)/3)
            segment_of_segment=int(segment/3)
            part = 0
            state = 0
            f.write('\nSignal from channel number(' + str(i+1) + ')\n')
            for part in range(0, 3):
                if(part==0):
                    f.write('focused part:::::::::\n')
                    ED_O2 = data[ (segment_of_segment) : (segment_of_segment*2) , i]
                    state = 1

                elif(part==1):
                    f.write('de - focused part:::::::::\n')
                    state=2
                    ED_O2 = data[ ( segment_of_segment + segment ) : ( segment_of_segment * 2+segment ), i]

                elif(part==2):
                    f.write('Third Part:::::::::\n')
                    state=3
                    ED_O2 = data[ ( 2*segment+segment_of_segment ): ( 2*segment + segment_of_segment * 2 ), i]


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

                
                if (part == 0):
                    delta_1 = delta_1 + delta_power
                    theta_1 = theta_1 + theta_power
                    alpha_1 = alpha_1 + alpha_power
                    beta_1 = beta_1 + beta_power
                    gamma_1 = gamma_1 + gamma_power
                elif (part == 1):
                    delta_2 = delta_2 + delta_power
                    theta_2 = theta_2 + theta_power
                    alpha_2 = alpha_2 + alpha_power
                    beta_2 = beta_2 + beta_power
                    gamma_2 = gamma_2 + gamma_power
                elif (part == 2):
                    delta_3 = delta_3 + delta_power
                    theta_3 = theta_3 + theta_power
                    alpha_3 = alpha_3 + alpha_power
                    beta_3 = beta_3 + beta_power
                    gamma_3 = gamma_3 + gamma_power



                f.write('Absolute delta power: %.3f uV^2\n' % delta_power)
                f.write('Absolute theta power: %.3f uV^2\n' % theta_power)
                f.write('Absolute alpha power: %.3f uV^2\n' % alpha_power)
                f.write('Absolute beta power: %.3f uV^2\n' % beta_power)
                f.write('Absolute gamma power: %.3f uV^2\n' % gamma_power)

            f.write('===========================================\n' )

        data_sample = [delta_1, theta_1, alpha_1, beta_1, gamma_1, 1]

        with open('dataset.csv', 'a') as csvFile:
            weiter = csv.writer(csvFile)
            weiter.writerow(data_sample)
        csvFile.close()

        data_sample = [delta_2, theta_2, alpha_2, beta_2, gamma_2, 2]

        with open('dataset.csv', 'a') as csvFile:
            weiter = csv.writer(csvFile)
            weiter.writerow(data_sample)
        csvFile.close()

        data_sample = [delta_3, theta_3, alpha_3, beta_3, gamma_3, 3]

        with open('dataset.csv', 'a') as csvFile:
            weiter = csv.writer(csvFile)
            weiter.writerow(data_sample)
        csvFile.close()

        f.write('#################################################\n')
        f.write('#################################################\n')
        f.write('#################################################\n')
        num_of_records=num_of_records+1

x=34*14
delta_1 /=x
theta_1 /= x
alpha_1 /=x
beta_1  /=x
gamma_1 /=x
f.write(str(delta_1))
f.write('\n')
f.write(str(theta_1))
f.write('\n')
f.write(str(alpha_1))
f.write('\n')
f.write(str(beta_1))
f.write('\n')
f.write(str(gamma_1))
f.write('\n')

SomeFns.plotband(delta_1 ,theta_1,alpha_1 ,beta_1 ,gamma_1)
#==========================
delta_2 /=x
theta_2 /= x
alpha_2 /=x
beta_2  /=x
gamma_2 /=x
SomeFns.plotband(delta_2,theta_2,alpha_2 ,beta_2 ,gamma_2)
f.write(str(delta_2))
f.write('\n')
f.write(str(theta_2 ))
f.write('\n')
f.write(str(alpha_2))
f.write('\n')
f.write(str(beta_2))
f.write('\n')
f.write(str(gamma_2))
f.write('\n')
#==========================
delta_3 /=x
theta_3 /= x
alpha_3 /=x
beta_3  /=x
gamma_3 /=x
SomeFns.plotband(delta_3 ,theta_3,alpha_3 ,beta_3,gamma_3)
f.write(str(delta_3))
f.write('\n')
f.write(str(theta_3 ))
f.write('\n')
f.write(str(alpha_3))
f.write('\n')
f.write(str(beta_3))
f.write('\n')
f.write(str(gamma_3))
f.write('\n')

print (num_of_records)

print ("5alasna")