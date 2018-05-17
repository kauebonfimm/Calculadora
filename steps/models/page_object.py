'''
Created on 6 de mai de 2018

@author: koliveirab
'''

class Page():
    
    def __init__(self,objeto):
        self.app=objeto
    
    
    def operacao(self,primeiro,segundo,operador):
        
        self.app.clica(primeiro, "name")
        self.app.clica(operador, "name")
        self.app.clica(segundo, "name")
        self.app.clica("=", "name")
        return self.app.pegar_texto("CalcText", "id")

    