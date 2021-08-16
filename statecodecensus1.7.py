import pytest
from StateCode_UC3 import StateCensusData, StateCensusAnalyzer, StateCode

class TestCensusDataWithCode():    

def test_type_mismatch_code(self):
        '''Function: test_type_mismatch_code check for type mismatch

            Function Parameters: self

            Return: None'''
        obj = StateCode('StateCode.csv')
        res = obj.type_mismatch()
        assert res == None
