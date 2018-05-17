#language:pt
Funcionalidade: Subtracao
	@CenarioSub1
  Esquema do Cenario: Subtracao com dois numeros
  	Dado Inserimos o valor <primeiro> 
  	Quando quando temos a subtracao do primeiro com <segundo>
  	Entao teremos o resultado:<resultados>
  Exemplos: 
      | primeiro  | segundo | resultados|
      | 1 				|     4 	|8|
      | 1 				|     2 	|90|
      
      
  @CenariosSub2
  Cenario: Subtracao com tres numeros
  	Dado Zeramos o nosso contador
  	Quando Inserimos o primeiro valor
  	E Somamos o segundo Valor
  	Entao Temos o valór de :
  	Mas e diferente de zero
  	
