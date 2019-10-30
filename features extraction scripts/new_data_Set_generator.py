import pandas as pd
import numpy as np
import SomeFns
import csv

class Data_Generator:
    name_of_the_file = ""
    log_file = ""
    source_of_data= ""
    num_of_records = 35
    num_of_channels= 14
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
        first_row = ["delta", "theta", "alpha", "beta", "gamma", "state"]
        with open(name+'.csv', 'w+') as csvFile:
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

    def Generate_Data(self,s=1,name="data"):
        """
            This Function is mainly the part responsible for generate the DataSet by
            extracting features from the dataset
            The name represent the name of the files that contain the data
            we will use the state for know how many samples to get from the data
        """
        self.state=s
        for file_number in range(1, self.num_of_records):
            """
                This loop just loop on all the records and read the data in array
            """
            name_of_file_to_read=self.source_of_data+'\\'+name+str(file_number)+'.csv'
            self.log_file.write("Reading now ===>> "+name_of_file_to_read+"\n")
            loadData = pd.read_csv( name_of_file_to_read )
            data = np.array(loadData)
            self.Divide_Data_the_generate(data)

    def Divide_Data_the_generate(self,data):
        """
            Assume We have a Record of length like This
                x x x x x x x x x
            We Assume that the parts that we shoud study should be these parts
                x   x x   x x   x    <<<==== Ignore these
                  x     x     x      <<<==== Study This
        """
        first_channel = data[:, 1]
        any_channel_length = len(first_channel)
        A = int(any_channel_length / 3)
        B = int( A / 3)
        """
            A ==> divide the whole record to 3 parts
            B ==> divide each part to 3 parts to take the one in the middle
        """
        first_region_dimentions = [ B     , 2*B    ]
        second_region_dimentions= [ A+B   , A+2*B  ]
        third_region_dimentions = [ 2*A+B , 2*A+2*B]
        """
            We have 2 options the first one to get one data sample from each region and the second is to 
            get 3 data sample from each region
        """
        if(self.state==1):
            self.Get_One_Sample_each_region(data,first_region_dimentions ,second_region_dimentions,third_region_dimentions)
        elif(self.state==3):
            self.Get_Three_Sample_each_region(data, first_region_dimentions, second_region_dimentions,third_region_dimentions)


    def Get_One_Sample_each_region( self, data,first_region ,second_region ,third_region):
        """
            This function is to loop in each region and get data sample in each one
        """
        first_data_sample= self.Get_data_Sample_from_region(data,first_region,1)
        second_data_sample = self.Get_data_Sample_from_region(data, second_region,2)
        third_data_sample = self.Get_data_Sample_from_region(data, third_region,3)
        self.Write_DataSample_in_The_CSV_file(first_data_sample)
        self.Write_DataSample_in_The_CSV_file(second_data_sample)
        self.Write_DataSample_in_The_CSV_file(third_data_sample)

    def Get_Three_Sample_each_region( self, data,first_region ,second_region ,third_region):
        """
            This function is to loop in each region and get 3 data samples in each one
            Assume we have each region like this:
                xxx
            we need to deal with each part alone like this:
                x x x
            This is not the best implementation for something like this function But this
            just to avoid any mistakes for now
        """
        #Divide 1st part to 3 parts
        len = first_region[1]-first_region[0]+1
        A = int(len/3)
        region_1 = [first_region[0]     , first_region[0]+A]
        region_2 = [first_region[0]+A   , first_region[0] + 2*A]
        region_3 = [first_region[0]+2*A , first_region[1]]
        first_data_sample_1 = self.Get_data_Sample_from_region(data,region_1,1)
        first_data_sample_2 = self.Get_data_Sample_from_region(data, region_2, 1)
        first_data_sample_3 = self.Get_data_Sample_from_region(data, region_3, 1)
        self.Write_DataSample_in_The_CSV_file(first_data_sample_1)
        self.Write_DataSample_in_The_CSV_file(first_data_sample_2)
        self.Write_DataSample_in_The_CSV_file(first_data_sample_3)

        # Divide 2nd part to 3 parts
        len = second_region[1] - second_region[0] + 1
        A = int(len / 3)
        region_1 = [second_region[0], second_region[0] + A]
        region_2 = [second_region[0] + A, second_region[0] + 2 * A]
        region_3 = [second_region[0] + 2 * A, second_region[1]]
        second_data_sample_1 = self.Get_data_Sample_from_region(data, region_1, 2)
        second_data_sample_2= self.Get_data_Sample_from_region(data, region_2, 2)
        second_data_sample_3 = self.Get_data_Sample_from_region(data, region_3, 2)
        self.Write_DataSample_in_The_CSV_file(second_data_sample_1)
        self.Write_DataSample_in_The_CSV_file(second_data_sample_2)
        self.Write_DataSample_in_The_CSV_file(second_data_sample_3)

        # Divide 3rd part to 3 parts
        len = third_region[1] - third_region[0] + 1
        A = int(len / 3)
        region_1 = [third_region[0], third_region[0] + A]
        region_2 = [third_region[0] + A, third_region[0] + 2 * A]
        region_3 = [third_region[0] + 2 * A, third_region[1]]
        third_data_sample_1 = self.Get_data_Sample_from_region(data, region_1, 3)
        third_data_sample_2 = self.Get_data_Sample_from_region(data, region_2, 3)
        third_data_sample_3 = self.Get_data_Sample_from_region(data, region_3, 3)
        self.Write_DataSample_in_The_CSV_file(third_data_sample_1)
        self.Write_DataSample_in_The_CSV_file(third_data_sample_2)
        self.Write_DataSample_in_The_CSV_file(third_data_sample_3)

    def Get_data_Sample_from_region( self, data, region , state):
        """
            This function just take the region of the datasample and it loop on all the channels to calculate the
            avg power from all of them
        """
        data_sample=[0,0,0,0,0,state]
        for channel in range(0, self.num_of_channels):
            data_part=data[region[0]:region[1],channel]
            # Define the duration of the window to be 4 seconds
            win_sec = 4
            # Compute average absolute power of Delta band
            delta_power = SomeFns.bandpower(data_part, self.sf, [0.5, 4], win_sec)
            data_sample[0]+=delta_power
            # Compute average absolute power of Theta band
            theta_power = SomeFns.bandpower(data_part, self.sf, [4, 8], win_sec)
            data_sample[1] +=theta_power
            # Compute average absolute power of Alpha band
            alpha_power = SomeFns.bandpower(data_part, self.sf, [8, 12], win_sec)
            data_sample[2] +=alpha_power
            # Compute average absolute power of Beta band
            beta_power = SomeFns.bandpower(data_part, self.sf, [12, 30], win_sec)
            data_sample[3] +=beta_power
            # Compute average absolute power of Gamma band
            gamma_power = SomeFns.bandpower(data_part, self.sf, [30, 100], win_sec)
            data_sample[4] +=gamma_power
        for feature in range(0, 5):
            data_sample[feature]=data_sample[feature]/self.num_of_channels
        return data_sample

def main():
    #create file to put the data in it
    Data_Gen = Data_Generator("data_set_file")
    Data_Gen.Read_Data_from_Folder("EEG DATA CSV after filtering")
    """
        The number that next function takes determines tha number of datasambles taken from the same record 
    """
    Data_Gen.Generate_Data(3)

if __name__ == "__main__":
    main()