import pandas as pd
import numpy as np
import SomeFns
import csv

class Data_Generator:
    name_of_the_file = ""
    log_file = ""
    source_of_data= ""
    num_of_records = 1
    #must defined before run the script
    num_of_expected_data_samples=40
    #================================
    num_of_channels= 14
    """
        selective_channels option will control what is the channels you want to include in your dataset
    """
    selective_channels = [1,2, 3,4,5, 6, 7, 8, 9,10,11,12,13, 14]
    #selective_channels=[2,3,6,7,8,9,14]
    sf=128
    state=1
    def __init__(self,name="",log_file_name="logs"):
        self.make_new_csv_file_for_data(name)
        self.open_log_file_for_writing(log_file_name)

    def make_new_csv_file_for_data(self,name):
        """
            This Function just make new file with the file name to put data in it
            make the first row define what we have in each coloum
            make sure theirs no file has the same name that you input it
        """
        self.name_of_the_file=name+'.csv'
        """
            for old approach:
            first_row = ["delta", "theta", "alpha", "beta", "gamma", "state"]    
        """
        """
        If you want selective channels
        first_row = ["delta ch(2)", "theta ch(2)", "alpha ch(2)", "beta ch(2)", "gamma ch(2)",
                     "delta ch(3)", "theta ch(3)", "alpha ch(3)", "beta ch(3)", "gamma ch(3)",
                     "delta ch(6)", "theta ch(6)", "alpha ch(6)", "beta ch(6)", "gamma ch(6)",
                     "delta ch(7)", "theta ch(7)", "alpha ch(7)", "beta ch(7)", "gamma ch(7)",
                     "delta ch(8)", "theta ch(8)", "alpha ch(8)", "beta ch(8)", "gamma ch(8)",
                     "delta ch(9)", "theta ch(9)", "alpha ch(9)", "beta ch(9)", "gamma ch(9)",
                     "delta ch(14)", "theta ch(14)", "alpha ch(14)", "beta ch(14)", "gamma ch(14)", "state"]
        """
        first_row = ["delta ch(1)", "theta ch(1)", "alpha ch(1)", "beta ch(1)", "gamma ch(1)",
                     "delta ch(2)", "theta ch(2)", "alpha ch(2)", "beta ch(2)", "gamma ch(2)",
                     "delta ch(3)", "theta ch(3)", "alpha ch(3)", "beta ch(3)", "gamma ch(3)",
                     "delta ch(4)", "theta ch(4)", "alpha ch(4)", "beta ch(4)", "gamma ch(4)",
                     "delta ch(5)", "theta ch(5)", "alpha ch(5)", "beta ch(5)", "gamma ch(5)",
                     "delta ch(6)", "theta ch(6)", "alpha ch(6)", "beta ch(6)", "gamma ch(6)",
                     "delta ch(7)", "theta ch(7)", "alpha ch(7)", "beta ch(7)", "gamma ch(7)",
                     "delta ch(8)", "theta ch(8)", "alpha ch(8)", "beta ch(8)", "gamma ch(8)",
                     "delta ch(9)", "theta ch(9)", "alpha ch(9)", "beta ch(9)", "gamma ch(9)",
                     "delta ch(10)", "theta ch(10)", "alpha ch(10)", "beta ch(10)", "gamma ch(10)",
                     "delta ch(11)", "theta ch(11)", "alpha ch(11)", "beta ch(11)", "gamma ch(11)",
                     "delta ch(12)", "theta ch(12)", "alpha ch(12)", "beta ch(12)", "gamma ch(12)",
                     "delta ch(13)", "theta ch(13)", "alpha ch(13)", "beta ch(13)", "gamma ch(13)",
                     "delta ch(14)", "theta ch(14)", "alpha ch(14)", "beta ch(14)", "gamma ch(14)", "state"]
        with open(name+'.csv', 'a') as csvFile:
            w = csv.writer(csvFile)
            w.writerow(first_row)
        csvFile.close()

    def open_log_file_for_writing(self, name):
        """
            This function is just to open the log file to write some logs
        """
        self.log_file = open(name+".txt", "w+")

    def Read_Data_from_Folder(self, name):
        """
            This Function is only to define the path of your data to read and extract
            the features from it
        """
        self.source_of_data=name

    def Write_DataSample_in_The_CSV_file(self, datasample):
        """
            This Function is just to add new datasample in your dataSet file
        """
        with open(self.name_of_the_file, 'a') as csvFile:
            w = csv.writer(csvFile)
            w.writerow(datasample)
        csvFile.close()

    def Generate_Data(self,s=1,name="DataRecorded"):
        """
            This Function is mainly the part responsible for generate the DataSet by
            extracting features from the dataset
            The name represent the name of the files that contain the data
            we will use the state for know how many samples to get from the data
        """
        for sample in range(1,self.num_of_expected_data_samples+1):
            data=np.array([[]])
            self.state=s
            for file_number in range(1, 31):
                """
                    This loop just get data from 30 second 
                """
                name_of_file_to_read=self.source_of_data+'\\'+name+str(self.num_of_records)+'.csv'
                self.num_of_records=self.num_of_records+1
                self.log_file.write("Reading now ===>> "+name_of_file_to_read+"\n")
                loadData = pd.read_csv( name_of_file_to_read )
                temp_data = np.array(loadData)
                if(file_number==1):
                    data=temp_data
                else:
                    data=np.concatenate((data,temp_data),axis=0)
                #self.Divide_Data_the_generate(data)
            print(np.size(data, 0))
            print(np.size(data, 1))
            first_data_sample = self.Get_data_Sample_from_region(data, self.state)
            self.Write_DataSample_in_The_CSV_file(first_data_sample)

    def Get_data_Sample_from_region( self, data, state):
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
        for channel in self.selective_channels:
            """
                if data is filtered:
                data_part=data[region[0]:region[1],channel-1]
            """
            data_part=data[:,channel+1]
            # Define the duration of the window to be 4 seconds
            win_sec = 4
            # Compute average absolute power of Delta band
            delta_power = SomeFns.bandpower(data_part, self.sf, [0.5, 4], win_sec)
            data_sample[0]+=delta_power
            new_data_sample.append(delta_power)
            # Compute average absolute power of Theta band
            theta_power = SomeFns.bandpower(data_part, self.sf, [4, 8], win_sec)
            data_sample[1] +=theta_power
            new_data_sample.append(theta_power)
            # Compute average absolute power of Alpha band
            alpha_power = SomeFns.bandpower(data_part, self.sf, [8, 12], win_sec)
            data_sample[2] +=alpha_power
            new_data_sample.append(alpha_power)
            # Compute average absolute power of Beta band
            beta_power = SomeFns.bandpower(data_part, self.sf, [12, 30], win_sec)
            data_sample[3] +=beta_power
            new_data_sample.append(beta_power)
            # Compute average absolute power of Gamma band
            gamma_power = SomeFns.bandpower(data_part, self.sf, [30, 100], win_sec)
            data_sample[4] +=gamma_power
            new_data_sample.append(gamma_power)
        for feature in range(0, 5):
            data_sample[feature]=data_sample[feature]/self.num_of_channels
        """
            if you want the old approach of 5 numbers per each datasample use this line
            #return data_sample
        """
        new_data_sample.append(state)
        return new_data_sample

def main():
    #create file to put the data in it
    Data_Gen = Data_Generator("data_set_file")
    #Data_Gen.Read_Data_from_Folder("Data with filteration")
    Data_Gen.Read_Data_from_Folder("karaman foucsed")
    """
        The number that next function takes determines tha number of datasambles taken from the same record 
    """
    Data_Gen.Generate_Data(1)

if __name__ == "__main__":
    main()