import pytest
from StateCode_UC3 import StateCensusData, StateCensusAnalyzer, StateCode

import pytest
from StateCode_UC3 import StateCensusData, StateCensusAnalyzer, StateCode

class TestCensusDataWithCode():

    def test_type_mismatch_census(self):
        '''Function: test_type_mismatch_census check for type mismatch

            Function Parameters: self

            Return: None
            '''
        obj = StateCensusAnalyzer('StateCensusData.csv')
        res = obj.type_mismatch()
        assert res == None

    def test_delimiter_census(self):
        '''Function: test_delimiter_census check for delimiter mismatch

            Function Parameters: self

            Return: None'''
        obj = StateCensusAnalyzer.read('StateCensusData.csv')
        res = obj.detect_delimiter()
        assert res == None

    def test_header_census(self):
        '''Function: test_header_census check for header mismatch

            Function Parameters: self

            Return: None
            '''
        obj = StateCensusAnalyzer.read('StateCensusData.csv')
        res = obj.header_check()
        assert res == None
