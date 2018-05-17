'''
Created on 27 de abr de 2018

@author: koliveirab
'''
import unittest
from PyDeskAutomator import Desk

class Test(unittest.TestCase):


    def testName(self):
        self.app=Desk()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()