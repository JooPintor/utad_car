## Criação de projetos no ROS

Para iniciar qualquer tipo de projecto em ROS é sempre necessario de criar um workspace para conter os modulos que serão utilizados para a contrução. Em ROS nos utilizamos a farrememta **Catkin** como não só o nosso repositorio dos modulos mas tamebem o nosso workspace para fazer a compilação dos nossos programas para o ROS.

Primeiro é preciso decidir para onde iremos colocar o nosso workspace, é aconcelhado por num sitio que seja de facil acesso que varias das linhas de comando utilizados vão chamar o caminho um grando numero de vezes, ao escolher onde vamos por o catkin workspace iremos escrever na cmd:

     mkdir -p ~/catkin_ws/src
     cd ~/catkin_ws/
     catkin_make

How executar estas linhas de codigo iremos criar as pastas src e devel, src será onde vamos por os nosssos modulos e nodes do nosso projeto e dentro de devel irá conter o nosso setup.bash, sendo este necessario de ser executado cada vez que intrudozimos algo de novo no nosso projeto, para que seja introduzido no projeto a nova informação, escrevendo:

      source devel/setup.bash
(Nota: para verificar que o caminho do catkin workspace esta a utilizar a versão do ROS que este foi feito escreve-se echo $ROS_PACKAGE_PATH.)
