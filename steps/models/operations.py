'''
Created on 26 de abr de 2018

@author: koliveirab
'''

class Operacao():
    '''
    Escolher um operador apartir de um testo simples
    '''
    def __init__(self):
        self
    
    @staticmethod
    def operador(operador):
        if(operador=="soma"):
            operation="+"
        elif(operador=="subtracao"):
            operation="-"
        elif(operador=="divisao"):
            operation=u"/"
        elif(operador=="multiplicacao"):
            operation="X"
        elif(operador=="igual"):
            operation="="
        print(operation)
        return operation