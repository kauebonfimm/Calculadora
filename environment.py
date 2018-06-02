'''


@author: kauebonfim
'''

from Pyautomators.Pydeskautomator import Desk
from behave import *
from Pyautomators import Pyambautomator
from time import sleep
from steps.models.operations import Operacao
from libss.metodos import Strings
from Pyautomators import Pyassertautomator,Pydocautomator

def before_all(context):
    context.path=Pyambautomator.caminho_ate_pasta()
    context.calc=Desk(caminho_driver=context.path+"drivers/", aplicacao=context.path+"drivers/Calculator.exe")
    context.operador=Operacao()
    context.asserts=Pyassertautomator
    context.doc=Pydocautomator
    
def before_features(context,feature):
    pass

def before_scenario(context,scenario):
    pass
    
    
def before_step(context,step):
    context.seqP=" "
    sleep(3)
    
    
def after_step(context,step):
    context.prints="{}{}".format(str(context.scenario).replace("<",' ').replace(">",' ').replace('"',' '),str(step.name).replace("<",' ').replace(">",' ').replace('"',' '))
    context.doc.printarTela(context.path+"docs/"+context.prints+".png")
    

def after_scenario(context,scenario):
    sleep(2)
    context.calc.clica("C","name")

def after_feature(context,feature):
    pass

def after_all(context):
    context.calc.fechar_programa()
