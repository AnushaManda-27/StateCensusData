import pytest
from StateCode_UC3 import StateCensusData, StateCensusAnalyzer, StateCode

class TestCensusDataWithCode():
    def test_delimiter_census(self):
        '''Function: test_delimiter_census check for delimiter mismatch

            Function Parameters: self

            Return: None'''
        obj = StateCensusAnalyzer.read('StateCensusData.csv')
        res = obj.detect_delimiter()
        assert res == None
