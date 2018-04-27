'''
Created on 26 de abr de 2018

@author: koliveirab
'''

from PyDeskAutomator import Desk
from behave import *
import Pyambautomator
from time import sleep
from steps.models.operations import Operacao
from libss.metodos import Strings
import Pyassertautomator

def before_all(context):
    context.path=Pyambautomator.caminho_anterior()
    context.calc=Desk(caminho_driver=context.path+"/drivers/", aplicacao=context.path+"/drivers/Calculator.exe")
    context.operador=Operacao()
    context.asserts=Pyassertautomator
    
    
def before_features(context,feature):
    print()

def before_scenario(context,scenario):
    print()

def before_steps(context,step):
    print(step.name)

def after_steps(context,step):
    pass

def after_scenario(context,scenario):
    sleep(2)
    context.calc.clica("C","name")

def after_feature(context,feature):
    pass

def after_all(context):
    context.calc.fechar_programa()
