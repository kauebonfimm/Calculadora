Feature: Soma
	@CenarioSoma1
  Scenario Outline: Soma com dois numeros
  	Given Inserimos o valor <primeiro> 
  	When quando temos a soma do primeiro com <segundo>
  	Then teremos o resultado:<resultados> 
  Examples: 
      | primeiro  | segundo | resultados|
      | 1					|     2 	|			8			|
      | 1 				|     3 	|			4			|
      
      
  @CenarioSoma2
  Scenario: Soma com tres numeros
  	Given Zeramos o nosso contador
  	When Inserimos o primeiro valor
  	And Somamos o segundo Valor
  	Then Temos o valor de :
  	But e diferente de zero
  	

  