'''
Created on 27 de abr de 2018

@author: koliveirab
'''

import os


os.chdir("feature")
print(os.path.dirname(os.getcwd()))
os.system("python -m behave")
print("teste iniciado")