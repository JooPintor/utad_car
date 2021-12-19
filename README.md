# Objetivo

Esta pagina tem o objectivo de ser um depositorio de conhecimento para o ensino de utilização do ROS e introdução à visão dos robos.

Para a realização deste trabalho, foram utilizados os equipamentos indicados no documento ["Equipamentos Utilizados"](./docs/Equipamento%20Utilizado.md), com os quais foram realizados diversos estudos, sendo registadas as principais dificudades encontradas, bem como o modo de as ultrapassar, nos casos em que tal ocorreu.

## Temas abordados
- [O que é o ROS?](#o-que-é-ROS)
- Instalação do SO nos SBC
- Instalação do ROS
- Insatalação de Divers dos Motores
- Insatalação dos Codificadores
- Montagem do Robot
- Instalação do RobotPeak Lidar
- Instalação da Camera Intel RealSense
- Processamento de Imagem
- Deteção de obstaculos

## O que é ROS?
O __Robot Operating System__ (ROS, sistema operativo de robôs) é uma coleção de frameworks de software para desenvolvimento e programação de robôs, que fornece as funcionalidades dum sistema operativo num cluster de computadores heterogêneo.

O ROS fornece serviços normalmente fornecidos pelos sistemas operativos, tais como abstração de hardware, controle de dispositivos de baixo nível, a implementação de funcionalidades comumente usadas, passagem de mensagens entre processos e gestão de pacotes.

O conjuntos de processos do ROS em execução são representados numa arquitetura gráfica onde o processamento é realizado nos nós que podem receber e enviar mensagens, tais como valores de sensores, controle, estado, planeamento, atuadores e outras.

Apesar da importância da reatividade e baixa latência no controle de robôs, o ROS em si, não é um sistema operativo de tempo real, embora seja possível integrar o ROS com código em tempo real.

O Software do ecossistema ROS pode ser dividido em três grupos:
- Ferramentas independentes da linguagem e plataforma usadas para a construção e distribuição de software baseado em ROS;
- Implementações de bibliotecas clientes de ROS como roscpp, rospy e roslisp;
- Pacotes com código relacionado com aplicações que usam uma ou mais bibliotecas cliente de ROS.

Tanto as ferramentas independentes da língua como as principais bibliotecas clientes (C++, Python e Lisp) são lançadas sob os termos da licença BSD, e como tal são softwares de fonte aberta e livre para uso comercial e de investigação.

A maioria dos outros pacotes estão licenciados sob uma variedade de licenças de código aberto. Estes outros pacotes implementam funcionalidades e aplicações, tais como drivers de hardware, modelos de robôs, tipos de dados, planeamento, percepção, mapeamento e localização simultâneos, ferramentas de simulação e outros algoritmos comumente usados.

 Para saber mais pode-se ir ao site do ["ROS"](http://wiki.ros.org/)

## Instalação do SO nos SBC
O sistema operativo que foi escolhido para este trabalho foi o sistema Linux, Ubuntu 18.04. O motivo para asta escolha é por ser o mais apropriado para a versão de ROS que nos utilizamos, o ROS melodic, sendo este um que possui certos pacotes e funções que estão só preparados para essa versão do Ubuntu e por causa do Rasperri Pi 3, que o proprio circuito só conseguio fazer o setup do SO desta versão, sendo que quando usamos a mais recente o RPI3 tem dificuldades em começar o proprio sistema. Tambem se tentou instalar na placa NVIDEA jetson o SO mas esse deu ainda piores resultados, sendo a placa inentulizavel para o trabalho quando se tentou fazer o setup.

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
