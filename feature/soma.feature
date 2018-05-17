#language:pt
Funcionalidade: Soma
	@CenarioSoma1
  Esquema do Cenario: Soma com dois numeros
  	Dado Inserimos o valor <primeiro> 
  	Quando quando temos a soma do primeiro com <segundo>
  	Entao teremos o resultado:<resultados> 
  Exemplos: 
      | primeiro  | segundo | resultados|
      | 1					|     2 	|			8			|
      | 1 				|     3 	|			4			|
      
      
  @CenarioSoma2
  Cenario: Soma com tres numeros
  	Dado Zeramos o nosso contador
  	Quando Inserimos o primeiro valor
  	E Somamos o segundo Valor
  	Entao Temos o valór de :
  	Mas e diferente de zero
  	

  