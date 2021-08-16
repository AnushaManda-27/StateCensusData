import pytest
from StateCode_UC3 import StateCensusData, StateCensusAnalyzer, StateCode

class TestCensusDataWithCode():

    def test_delimiter_code(self):
        '''Function: test_delimiter_code check for delimiter mismatch

            Function Parameters: self

            Return: None'''
        obj = StateCode.read('StateCode.csv')
        res = obj.detect_delimiter()
        assert res == None
