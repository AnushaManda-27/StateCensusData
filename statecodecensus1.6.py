import pytest
from StateCode_UC3 import StateCensusData, StateCensusAnalyzer, StateCode

class TestCensusDataWithCode():


    def test_header_code(self):
        '''Function: test_header_code check for header mismatch

            Function Parameters: self

            Return: None'''
        obj = StateCode.read('StateCode.csv')
        res = obj.header_check()
        assert res == None
