'''
Created on 26 de abr de 2018

@author: koliveirab
'''

import Pydocautomator
import Pyambautomator
import re
if __name__ == '__main__':
    path=Pyambautomator.path_atual()
    arquivo=str(path).replace("/tools", "")+"/feature/reports/teste.json"
    Pydocautomator.tranforma_cucumber(arquivo, arquivo)