
'''@Author: Anusha Manda
@Date: 05-08-2021 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 05-08-2021 18: 00: 30
@Title: Reading csv files using Exceptions
'''


import csv
import os


class StateCodes(Exception):

        def __init__(self):
              pass

        def records(content):
            '''
            Function: records is define to get number of records in a given file
                
                Function parameters: content (csv data after converting to list)
                
                Return : no_of_recors (length of csv list)
                '''
            no_records = len(content)
            return no_records


        def type_mismatch(file_name):
            ''' Function: type_mismacth is defined to check whethertype of file is .csv or not
            
                Function parameters: file_name
                
                Return: file_extension
                
                '''
            split = file_name
            ext = (os.path.splitext(split))
            file_extension = ext[1]
            if file_extension != '.csv':
                raise Exception("Type Mismatch")
            else:
                return file_extension

        def header_check(header):
            '''
            Function: header_check is defined to check header is correct or not

            Function Parameters: header

            Return: 'Header Matches'
            '''
            if header != ['State', 'Population', 'AreaInSqKm', 'DensityPerSqKm']:
                raise Exception("Header Mismatch")
            else:
                return 'Header Matches'


def read(filename):
    '''Function: read is defined to open given file, 
                check for file name mismatches and also to print the data in file.
        Function Parameters: filename

        Return: data[1:] (Except header), data[0] (only header)
    '''
    with open(filename, 'r') as csv_file:
        try:
            if csv_file.name != 'StateCensusData.csv':
                raise Exception
        except Exception:
            print("File name is incorrect")
        else:
            csv_read = csv.reader(csv_file, delimiter= ",")
            print(csv_read)

            data = []
            for line in csv_read:
                data.append(line)
            print(data)
            return data[1:], data[0]


if __name__ == '__main__':

    file_name = 'StateCensusData.csv'

    info, header = read(file_name)
    print(header)
    rec = StateCodes.records(info)
    print(rec)


    typedata = StateCodes.type_mismatch(file_name)
    print(typedata)

    head = StateCodes.header_check(header)
    print(head)
