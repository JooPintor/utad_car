### Fontes de alimentação

O “utad_car” utiliza duas fontes de alimentação independentes.

A principal motivação da utilização de fontes independentes resulta do facto dos motores de tração apresentarem grandes flutuações no consumo, o que leva á instabilidade da alimentação do Raspberry levado mesmo a que este momentaneamente se desligue.

De notar que embora tenha optado por utilizar fontes de 5V quer para o Raspberry quer para os motores, em caso de necessidade os motores poderiam ser alimentados com tensões superiores, como se poderá ver nas características do modulo _"Stepper Motor HAT"_.

Para a alimentação do Raspberry escolhi o _‘Power Bank D2375’_ cedida pela universidade que tem as seguintes características:

![Power Bank D2375](../imgs/Power%20Bank%20D2375.jpg)

Características:

	           Input : 5V/1A
	        Output : DC 5V/2.1A
	Capacidade : 5600 mAh


Para a alimentação dos motores recorri a _‘Power Banks’_ baseados em módulos de regulação da tensão de entrada e de saída, associados a uma bateria do tipo BRC 18650 de 3,7 V e com capacidades variáveis.
 
As características dos módulos de entrada e saída são as seguintes:

 	           Input : 5V/500 mA
	        Output : DC 5V/1A

