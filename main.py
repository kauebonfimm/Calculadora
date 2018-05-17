'''
Created on 27 de abr de 2018

@author: koliveirab
'''

from Pyautomators import Pyambautomator
from Pyautomators import Pydocautomator
from time import sleep
if(__name__=="__main__"):
    
    
    Pyambautomator.irDiretorio("feature")
    path=Pyambautomator.caminho_ate_pasta()
    print(path)
    Pyambautomator.execute("python -m behave")
    arquivo=str(path)+"/feature/reports/teste.json"
    print(arquivo)
    Pydocautomator.tranforma_cucumber(arquivo, arquivo)