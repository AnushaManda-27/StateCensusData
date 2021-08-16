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
