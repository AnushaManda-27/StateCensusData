import pytest
from StateCode_UC3 import StateCensusData, StateCensusAnalyzer, StateCode

class TestCensusDataWithCode():
    def test_records_census(self):
        '''Function: test_record_census check for number of records mismatch

            Function Parameters: self

            Return: None'''
        obj = StateCensusAnalyzer.read('StateCensusData.csv')
        res = obj.records()
        assert res == 29
