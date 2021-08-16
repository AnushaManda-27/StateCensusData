import pytest
from StateCode_UC3 import StateCensusData, StateCensusAnalyzer, StateCode

class TestCensusDataWithCode():

    def test_header_census(self):
        '''Function: test_header_census check for header mismatch

            Function Parameters: self

            Return: None
            '''
        obj = StateCensusAnalyzer.read('StateCensusData.csv')
        res = obj.header_check()
        assert res == None
