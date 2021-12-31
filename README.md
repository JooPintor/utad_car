# Objetivo

Esta página tem o objetivo de ser um repositório de conhecimento para o ensino de utilização do ROS e introdução à visão dos robots.

Para a realização deste trabalho, foram utilizados os equipamentos [aqui](./docs/Equipamento%20Utilizado.md) descritos, com os quais foram realizados diversos estudos, sendo registadas as principais dificuldades encontradas, bem como o modo de as ultrapassar, nos casos em que tal ocorreu.

Os estudos foram acompanhados e suportados pela montagem de um robot a que chamei "utad_car".

Os modulos ROS criados para controlar o "utad_car" são descritos nos temas abordados.

## Temas abordados
- [O que é o ROS?](#o-que-é-ros)
- Como iniciar um projeto em ROS?
- [Instalação do SO nos SBC](./docs/Instalação%20do%20SO%20nos%20SBC.md)
- [Instalação do ROS](./docs/Instalação%20do%20ROS.md)
- [Controlo dos Motores de Tração](./docs/Controlo%20dos%20Motores%20de%20tração.md)
- Instalação dos Codificadores
- Montagem do Robot
- Instalação do RobotPeak Lidar
- Instalação da Camera Intel RealSense
- Processamento de Imagem
- Deteção de obstáculos

## O que é ROS?
O __Robot Operating System__ (ROS, sistema operativo de robôs) é uma coleção de frameworks de software para desenvolvimento e programação de robôs, que fornece as funcionalidades dum sistema operativo num cluster de computadores heterogêneo.

O ROS fornece serviços normalmente fornecidos pelos sistemas operativos, tais como abstração de hardware, controle de dispositivos de baixo nível, a implementação de funcionalidades comumente usadas, tais como passagem de mensagens entre processos e gestão de pacotes.

O conjunto de processos do ROS em execução são representados numa arquitetura gráfica onde o processamento é realizado nos nós que podem receber e enviar mensagens, tais como valores de sensores, controle, estado, planeamento, atuadores e outras.

Apesar da importância da reatividade e baixa latência no controle de robôs, o ROS em si, não é um sistema operativo de tempo real, embora seja possível integrar o ROS com código em tempo real.

O Software do ecossistema ROS pode ser dividido em três grupos:
- Ferramentas independentes da linguagem e plataforma usadas para a construção e distribuição de software baseado em ROS;
- Implementações de bibliotecas clientes de ROS como roscpp, rospy e roslisp;
- Pacotes com código relacionado com aplicações que usam uma ou mais bibliotecas cliente de ROS.

Tanto as ferramentas independentes da língua como as principais bibliotecas clientes (C++, Python e Lisp) são lançadas sob os termos da licença BSD, e como tal são softwares de fonte aberta e livre para uso comercial e de investigação.

A maioria dos outros pacotes estão licenciados sob uma variedade de licenças de código aberto. Estes outros pacotes implementam funcionalidades e aplicações, tais como drivers de hardware, modelos de robôs, tipos de dados, planeamento, perceção, mapeamento e localização simultâneos, ferramentas de simulação e outros algoritmos comumente usados.

 Para saber mais pode-se ir ao site do [ROS](http://wiki.ros.org/)


## Como iniciar um projeto em ROS?

Para iniciar qualquer tipo de projecto em ROS é sempre necessario de criar um workspace para conter os modulos que serão utilizados para a contrução. Em ROS nos utilizamos a farrememta **Catkin** como não só o nosso repositorio dos modulos mas tamebem o nosso workspace para fazer a compilação dos nossos programas para o ROS.

Primeiro é preciso decidir para onde iremos colocar o nosso workspace, é aconcelhado por num sitio que seja de facil acesso que varias das linhas de comando utilizados vão chamar o caminho um grando numero de vezes, ao escolher onde vamos por o catkin workspace iremos escrever na cmd:

     mkdir -p ~/catkin_ws/src
     cd ~/catkin_ws/
     catkin_make
How executar estas linhas de codigo iremos criar as pastas src e devel, src será onde vamos por os nosssos modulos e nodes do nosso projeto e dentro de devel irá conter o nosso setup.bash, sendo este necessario de ser executado cada vez que intrudozimos algo de novo no nosso projeto, para que seja introduzido no projeto a nova informação, escrevendo:

      source devel/setup.bash

##Instalação do ROS

O sistema operativo que foi escolhido para este trabalho foi o sistema Linux, Ubuntu 18.04. O motivo para asta escolha é por ser o mais apropriado para a versão de ROS que nos utilizamos, o ROS melodic, sendo este um que possui certos pacotes e funções que estão só preparados para essa versão do Ubuntu e por causa do Rasperri Pi 3, que o proprio circuito só conseguio fazer o setup do SO desta versão, sendo que quando usamos a mais recente o RPI3 tem dificuldades em começar o proprio sistema. Tambem se tentou instalar na placa NVIDEA jetson o SO mas esse deu ainda piores resultados, sendo a placa inentulizavel para o trabalho quando se tentou fazer o setup.

Para fazer o setup the ROS no sistema windows, neste caso no portatil que está indicado na lista de materiais, nos temos que seguir mais alguns passos em comparação com o Linux, que ao contrario do outro a linha de comando do windows é incapaz de buscar pacotes ou até mesmo fazer instalação de certos programas sem primeiro installar certas bibliotecas e funções para a execução de ROS. Um dos programas que se teve que installar, porque senão nem poderiamos criar nodes para o project, é o Visual Studio 2019.
O Visual Studio 2019 é necessario por varios motivos sendo algus deles o facto de não só nos dar VCPKG, que é algo que nôs permetirá utilizar os pacotes no proprio ROS, mas tambem o Windows 10 SDK(Software Develepment Kit), que irá permitir a criação dos programas no windows que podem ser usados no ROS.

Aseguir irá ser instalado, apartir da linha de comando como admistrador, o chocolatey. O chocolatry é o programa que nós ajudará fazer downloads dos pacotes que o ROS fará download de uma list especifica do site do proprio programa. Com ele irámos fazer download do git, sendo estes pacotes que darãonos a capacidade de install qualquer programa que possuio pacotes para fazer setup. Este passo é mais um extra mas para que tenhamos que constantemente o prompt do VS 2019, podemos criar um short-cut para ser mais rapido para executar o ROS.

Uma coisa que temos de ter em atenção ao fazer o processo de instalação é ter qualquer software de anti-virus e firewall completamente desativado, que durante o processo de instalação, como os pacotes e até mesmo o setup feito para o proprio ROS e chocolatey vem de uma fonte que não tem identificação, o anti-virus identificará sempre como um virus, impedindo de os executar, se tal caso acontecer, irás ter que desinstalar tudo, desativar qualquer tipo de proteção que o computador tenha e recomeçar a instalação.

##Instalação dos Divers dos Motores

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
