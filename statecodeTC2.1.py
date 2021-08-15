
'''@Author: Anusha Manda
@Date: 11-08-2021 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 11-08-2021 18: 00: 30
@Title: Reading csv files using Exceptions
'''

import statecensuscodes_UC2
import unittest



class TestStateCode(unittest.TestCase, Exception):

    res1, res2 = statecensuscodes_UC2.read('StateCensusData.csv')

    def test_no_of_records_happy_test_case(self):
        '''Function: test_no_of_records_happy_test_case checks the given test case

            Function paramerts: self

            Return: none
        '''

        res = statecensuscodes_UC2.StateCodes.records(TestStateCode.res1)
        self.assertEqual(res, 29)
