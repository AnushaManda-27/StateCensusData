
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

    def test_sad_test_case(self):
        '''Function: test_sad_test_case for filename (correct or incorrect)

            Function parameters: self

            Return:none
        '''
        res = statecensuscodes_UC2.read('StateCensusData.csv')
        with self.assertRaises(Exception):
            self.assertFalse(res)

    def test_type_error(self):
        '''Function: test_type_error check for type mismatch

            Function Parameters: self

            Return: None
        '''
        res = statecensuscodes_UC2.StateCodes.type_mismatch('StateCensusData.csv')
        with self.assertRaises(Exception):
            self.assertNotEqual(res, '.csv')

    def test_header_check(self):
        '''Function: test_header_check check for header mismatch

            Function Parameters: self

            Return: None
        '''
        res = statecensuscodes_UC2.StateCodes.header_check(TestStateCode.res2)
        with self.assertRaises(Exception):
            self.assertNotEqual(res, 'Header Matches')


if __name__ == '__main__':
    unittest.main()
