# Objetivo

Esta pagina tem o objectivo de ser um depositorio de conhecimento para o ensino de utilização do ROS e introdução à visão dos robos.

Para a realização deste trabalho, foram utilizados os equipamentos indicados no documento "Equipamentos Utilizados", com os quais foram realizados diversos estudos, sendo registadas as principais dificudades encontradas, bem como o modo de as ultrapassar, nos casos em que tal ocorreu.

** Temas abordados**
- O que é o ROS?
- Instalação do SO no SBC
- 

- O que é ROS?\n
Robot Operating System é o sistema mais utilizados nos ultimos anos quando se vem há robotica, sendo este uma framework crianda a partir da ligação de diferentes computadores que assim vai criar o seu proprio sistema operativo para o robo que está a ser programado, para comprir as suas funções.

- incluindo os links para fazer download

- Explicação de alguns dos processos

No começo deste trabalho, foi montado um carrinho simples que possui duas rodas motorizadas e uma roda na frente ao centro, tendo as placa RasperryPi 3 montada com o chapeu en-cima. A montagem que foi feita no RPI3 é feita para que tenhamos o numero de portas necessarias para fazer não só a ligação dos nossos motores para a placa mas tambem para efetuar a ligação da camera utilizada para a placa, uma coisa que se tem de ter em conta enquanto a esta montagem é o numero das portas utilizadas para transmitir a informação, sendo esses numeros que vamos indicar no codigo que irá controlar o output e input da nossa montagem.

O primeiro passo que se fez foi arranjar um cartão sd para install o sistema operativo Ubuntu versão 18.08, o motivo de ser esta versão e não a mais recente é pelo facto desta versão conter algumas funções e operações que permitam a utilização da camera que as versões mais recentes não pessuem, tendo ocorrido erros quando estas versões foram testadas.

Ao installar e fazer set-up do sistema operativo, foi instalado o ROS melodic para o projecto, tambem pode se testou instalar o ROS kinetic, no entanto, existem certas funções e operações que o kinectic não possui em comparação com o melodic para o que nos desejamos executar, dando algumas dificuldades durante o processo quando tentamos o utilizar. Para fazer a instalação, foi-se ao site do ROS.org e seguio-se os passo de instalação lá indicados. 

O catkin workspace, o espaço onde vai ser focado os nossos nodes para o trabalho, ouve alguma complicação no inicio, mas só por causa que não se percebia-se muito bem como o catkin_make funcionava. Ao perceber melhor o que catkin_make faz, e tambem perceber que tem se que executar o ficheiro setup.bat sempre que modificamos algo enquanto a direções e criações de nodes e pacotes, tornou-se mais facil de perceber como é que os pacotes e nodes se irão posicionar e ligar no catkin workspace.

Para modificar e escrever o codigo que se arranjou para o projecto foi utilizado o iditor de texto que já vinha no Ubuntu chamado Pluma, tambem se tentou escrever o codigo em c++ mas isso exigiu mais bibliotecas e funcões, que Ubuntu não pessuia, para conseguir fazer o codigo funcionar, fazer assim necessario fazer download disso tudo ocupando espaço que nos precisamos para o projeto, no entanto em python so teremos que fazer um simples apt get install para instalar o que for necessario, sendo isto não so mais rapido mas tambem mais eficiente para que o que for instalado seja utilizavel por qualquer aplicação.

Foi se fazer os exemplos que estão no site do ROS para começar a perceber a metedologia do firmware e para ajudar a perceber como as funções basicas que o ROS consegue fazer. Só depois de acabar de fazer o ultimo tutorial do nivel basico do ROS é que se começou a fazer os nodes para o projeto.
O primeiro node que se começou a tratar éra o que envolvia com o movimento das rodas, tendo em atenção que o codigo que foi arranjado na net foi modificado para que as saidas de output condizião com o comando desejado. Ao testars premeiro com comandos já dados no codigo, notou-se que havia uma diferença enquanto ao output dos pulsos dados nas saidas, tendo sido visto que éra um problema no motor em si, então foi substituido. Ao fazer mais alguns testes ao codigo, para saber como controlar a aceleração e movimento do carro, começou-se a por comandos de teclado a controlar para onde é que o carro irá se mover.

O passo que se fez aseguir foi a intrudoção da camera Intel Realsense D435, sendo esta uma camera que consegue ver profundidades.
Para conseguirmos fazer com que a camera seja utilizavel em ROS foi preciso arranjar um conjunto de pacotes especificos, chamado Realsense2, sendo este um dos principais ficheiros para os nossos nodes funcionarem com a camera da intel. Estes pacotes são sacados no proprio site da intel e tambem se pode fazer download do SDK, que é o software que ajuda a vizualizar o que a camera esta a ver e calcular as distancias.

Uma coisa que tive de aprender do ROS é o rviz, uma farrementa do ROS que é utilizado para a vizualização do robo que tenha camaras ou sensores.

- Algumas das dificuldades encontradas
- A explicação de como funciona
- Resultados Esperados
