'''
Created on 26 de abr de 2018

@author: koliveirab
'''
from behave import *
from time import sleep

@given("Inserimos o valor {primeiro}")
def inserir_valor(context,primeiro):
    context.calc.clica(primeiro,tipo="name")
    
    
@when("quando temos a {operador} do primeiro com {segundo}")
def operamos(context,operador,segundo):
    elemento=context.operador.operador(operador)
    context.calc.clica(elemento,"name")
    context.calc.clica(segundo,"name")
    
@then("teremos o resultado:{resultado}")
def resultado(context,resultado):
    context.calc.clica("=",tipo="name")
    resultados=context.calc.pegar_texto("CalcText","id")
    result=context.asserts.verifica_valor(resultados,resultado)
    
    
@given("Zeramos o nosso contador")
@when("Inserimos o primeiro valor")
@when("Somamos o segundo Valor")
@then("Temos o valor de :")
@then("e diferente de zero")
def step(context):
    pass