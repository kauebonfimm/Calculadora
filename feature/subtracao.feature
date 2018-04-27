Feature: Subtracao
	@CenarioSub1
  Scenario Outline: Subtracao com dois numeros
  	Given Inserimos o valor <primeiro> 
  	When quando temos a subtracao do primeiro com <segundo>
  	Then teremos o resultado:<resultados>
  Examples: 
      | primeiro  | segundo | resultados|
      | 1 				|     4 	|8|
      | 1 				|     2 	|90|
      
      
  @CenariosSub2
  Scenario: Subtracao com tres numeros
  	Given Zeramos o nosso contador
  	When Inserimos o primeiro valor
  	And Somamos o segundo Valor
  	Then Temos o valor de :
  	But e diferente de zero
  	
