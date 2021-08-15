
'''@Author: Anusha Manda
@Date: 11-08-2021 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 11-08-2021 18: 00: 30
@Title: Reading csv files using Exceptions
'''

import StateCensusData_UC1
import unittest
import os
os.chdir('C:\\Users\\M Veeraiah\\Desktop\\python_main\\Reading_writing_CSV')


class TestStatecensus(unittest.TestCase, Exception):

    

    def test_no_of_records_happy_test_case(self):
        '''Function: test_no_of_records_happy_test_case checks the given test case

            Function paramerts: self

            Return: none
        '''
        res1, res2 = StateCensusData_UC1.read('StateCensusData.csv')
        res = StateCensusData_UC1.IndianStatesInfo.records(res1)
        self.assertEqual(res, 29)


    def test_sad_test_case(self):
        '''Function: test_sad_test_case for filename (correct or incorrect)

            Function parameters: self

            Return:none
        '''
        res = StateCensusData_UC1.read('StateCensusData.csv')
        with self.assertRaises(Exception):
            self.assertFalse(res)
