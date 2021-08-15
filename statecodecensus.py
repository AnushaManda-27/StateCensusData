
'''@Author: Anusha Manda
@Date: 05-08-2021 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 05-08-2021 18: 00: 30
@Title: Creating child classes and writing data into csv
'''


import csv,os,json
from dotenv import load_dotenv
load_dotenv()


class StateCensusData():

    def __init__(self, filename):
        self.filename = filename
        
    
    def type_mismatch(self):
        ''' Function: type_mismacth is defined to check whethertype of file is .csv or not
            
            Function parameters: self
                
            Return: None
                
                '''
        try:
            if self.filename.split(".")[1] != 'csv':
                raise Exception
        except Exception:
            print("Type Mismatch")
        else:
            print("csv extension checked")

class StateCensusAnalyzer(StateCensusData):

    def __init__(self, filename, file_header=None, data=None):
        super().__init__(filename)
        if file_header is None:
            self.file_header = ""
        else:
            self.file_header = file_header

        if data is None:
            self.data = []
        else:
            self.data = data

    def detect_delimiter(self):
        ''''Description: detect_delimiter function id defined to check delimiter is correct or not
            Function Parameters: self
            Return: None'''
        try:
            if self.file_header.find(",") == -1:
                raise Exception
        except Exception:
            print("Delimiter Mismatch")
        else:
            print("Delimeter is checked")

    def header_check(self):
        '''Description: Function header_check is defined to check if header matches or not
            Function Parameters: self
            Return: None
        '''
        try:    
            if self.file_header != 'State,Population,AreaInSqKm,DensityPerSqKm':
                raise Exception
        except Exception:
            print("Header Mismatch")
        else:
            print('Header is checked')

    def records(self):
        '''
        Description: function record is defined to number of records matches correctly or not
            Function Parameters: self
            Return: None
            '''
        no_records = len(self.data)
        return no_records

    @classmethod
    def read(cls, file_name):
        '''
        Description: read() mfunction is defined to read the csv file and check if file matches 

        Function Parametrs: file_name
        Return: file_name, header, data
        '''
        with open(file_name, 'r') as csv_file:
            if csv_file.name != 'StateCensusData.csv':
                raise Exception("File name is incorrect")
            else:
                print('file name matching')
                csv_read = csv.DictReader(csv_file, delimiter=",")
                
                data = []
                for j in csv_read:
                    data.append(j)
                
                header = (",").join(list(data[0].keys()))
                return cls(file_name, header, data)    


class StateCode(StateCensusData):

    def __init__(self, filename, file_header=None, data=None):
        super().__init__(filename)
        if file_header is None:
            self.file_header = ""
        else:
            self.file_header = file_header

        if data is None:
            self.data = []
        else:
            self.data = data

    def detect_delimiter(self):
        ''''Description: detect_delimiter function id defined to check delimiter is correct or not
            Function Parameters: self
            Return: None'''

        try:
            if self.file_header.find(",") == -1:
                raise Exception
