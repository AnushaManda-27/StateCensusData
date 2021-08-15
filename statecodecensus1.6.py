
import pytest
from StateCode_UC3 import StateCensusData, StateCensusAnalyzer, StateCode

class TestCensusDataWithCode():

def test_records_code(self):
        '''Function: test_records_code check for number of mismatch

            Function Parameters: self

            Return: None'''
        obj = StateCode.read('StateCode.csv')
        res = obj.records()
        assert res == 37
