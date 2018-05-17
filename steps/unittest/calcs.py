'''
Created on 6 de mai de 2018

@author: koliveirab
'''
import unittest2
from PyDeskAutomator import Desk
import Pyambautomator
from time import sleep
from package.steps.models.page_object import Page
import timeout_decorator
import xmlrunner
import testtools 
class Test(unittest2.TestCase):


    def setUp(self):
        self.path=Pyambautomator.caminho_anterior().replace("/steps", "")
        self.app=Desk(caminho_driver=self.path+"/drivers/", aplicacao=self.path+"/drivers/Calculator.exe")
        self.page=Page(self.app)

    def tearDown(self):
        self.app.fechar_programa()

    
    def testSoma(self):
        sleep(3)
        valor=self.page.operacao("1", "2", "+")
        self.assertEqual(valor, "3", "VALOR FOI INVALIDO")
    
    
    def testSubtracao(self):
        sleep(3)
        valor=self.page.operacao("5", "2", "-")
        self.assertEqual(valor, "8", "VALOR FOI INVALIDO")
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest2.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
    suite = unittest2.TestLoader().loadTestsFromTestCase(Test)