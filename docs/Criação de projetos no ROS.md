## Criação de projetos no ROS
O ROS utiliza o [catkin](#Visão-geral-do-"catkin") como compilador, pelo que o mesmo deverá ser instalado antes de se começar a criar um projeto.


Antes de se poderem criar projetos em ROS é necessário ter o ROS instalado no equipamento em que se pretenda criar o projeto e .

A criação dos projetos no ROS deverá seguir as instruções da página ROS-Wiki Para iniciar qualquer tipo de projecto em ROS é sempre necessario de criar um workspace para conter os modulos que serão utilizados para a contrução. Em ROS nos utilizamos a farrememta **Catkin** como não só o nosso repositorio dos modulos mas tamebem o nosso workspace para fazer a compilação dos nossos programas para o ROS.

Primeiro é preciso decidir para onde iremos colocar o nosso workspace, é aconcelhado por num sitio que seja de facil acesso que varias das linhas de comando utilizados vão chamar o caminho um grando numero de vezes, ao escolher onde vamos por o catkin workspace iremos escrever na cmd:

     mkdir -p ~/catkin_ws/src
     cd ~/catkin_ws/
     catkin_make

How executar estas linhas de codigo iremos criar as pastas src e devel, src será onde vamos por os nosssos modulos e nodes do nosso projeto e dentro de devel irá conter o nosso setup.bash, sendo este necessario de ser executado cada vez que intrudozimos algo de novo no nosso projeto, para que seja introduzido no projeto a nova informação, escrevendo:

      source devel/setup.bash
(Nota: para verificar que o caminho do catkin workspace esta a utilizar a versão do ROS que este foi feito escreve-se echo $ROS_PACKAGE_PATH.)

## Visão geral do "catkin"
O __catkin__ é o compilador oficial do ROS e o sucessor do compilador original do ROS, o __rosbuild__. O __catkin__ combina macros _CMake_ e scripts _Python_ para permitir algumas funcionalidades para além do fluxo de trabalho normal do _CMake_. O __catkin__ foi projetado para ser mais convencional que o __rosbuild__, permitindo melhor distribuição de pacotes, melhor suporte de compilação cruzada e melhor portabilidade. O fluxo de trabalho do __catkin__ é muito semelhante ao do _CMake_, mas adiciona suporte para infraestrutura automática de 'localização de pacotes' e construção de vários projetos dependentes ao mesmo tempo.

O __catkin__ é responsável por gerar 'ficheiros_destino' a partir do código-fonte, que podem ser usados por um utilizador final. Esses ficheiros podem ter a forma de bibliotecas, programas executáveis, scripts gerados, interfaces exportadas (por exemplo, arquivos de cabeçalho C ++) ou qualquer outra coisa que não seja um código estático. Na terminologia ROS, o código-fonte é organizado em 'pacotes', onde cada pacote normalmente consiste em um ou mais ficheiros quando compilado.

Para saber mais sobre o __catkin__ [consultar a página](https://wiki.ros.org/catkin/conceptual_overview).

