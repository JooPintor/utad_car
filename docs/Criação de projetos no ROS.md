## Criação de projetos no ROS
O ROS utiliza o [catkin](#Visão-geral-do-catkin) como compilador, pelo que o este deverá ser [instalado](#Instalação-do-catkin) antes de se começar a criar um projeto.

A utilização do __catkin__ presupõe que o mesmo esteja instalado e referenciado no ambiente de trabalho.No caso da sua instalação com o comando _"apt-get"_, deve ser utilizado um dos seguintes comandos em função das versões de ROS:

     Para ROS melodic:
     
     source /opt/ros/melodic/setup.bash

     Para ROS noetic:
     
     source /opt/ros/noetic/setup.bash

Para a criação do espaço de trabalho poderão se utilizados o seguintes comandos:

     mkdir -p ~/catkin_ws/src
     cd ~/catkin_ws/
     catkin_make

Note-se que neste exemplo estamos a criar o espaço de trabalho na pasta "~/catkin_ws" mas poderia ser utilizada qualquer outra pasta que nos fossse conveniente.

O comando "catkin_make" é um comando util para trabalhar com espaços de trabalho catkin. Ao executa-lo pela primeira vez na área de trabalho, ele cria o ficheiro _"CMakeLists.txt"_ na pasta _'src'_, com os links necessários.

Além disso, na pasta do ambiente de trabalho serão cridas duas novas pastas: _'build'_ e _'devel'_. Na pasta _'devel'_, são criados vários arquivos setup. * Sh, que permitem através do comando "source" sobrepor este espaço de trabalho ao ambiente de trabalho inical.

Para terminar deve-se fazer o 'source' da área de trabalho com o comando:

      source devel/setup.bash

E verificada a configuração com o coamndo:

     echo $ROS_PACKAGE_PATH
     
     Resultado no ROS melodic:
     /home/ap/catkin_ws/src:/opt/ros/melodic/share
          
     Resultado no ROS noetic:
     /home/ap/catkin_ws/src:/opt/ros/noetic/share

Para mais informação sobre a criação do espaço de trabalho para um projeto deverá ser consultada [esta](http://wiki.ros.org/catkin/Tutorials/create_a_workspace) página.

Para a utilização das áreas de trabalho nos projetos deverá ser consultada [esta](http://wiki.ros.org/catkin/Tutorials/using_a_workspace) página.

## Visão geral do "catkin"
O __catkin__ é o compilador oficial do ROS e o sucessor do compilador original, o __rosbuild__. O __catkin__ combina macros _CMake_ e scripts _Python_ para permitir algumas funcionalidades para além do fluxo de trabalho normal do _CMake_. O __catkin__ foi projetado para ser mais convencional que o __rosbuild__, permitindo melhor distribuição de pacotes, melhor suporte de compilação cruzada e melhor portabilidade. O fluxo de trabalho do __catkin__ é muito semelhante ao do _CMake_, mas adiciona suporte para infraestrutura automática de 'localização de pacotes' e construção de vários projetos dependentes ao mesmo tempo.

O __catkin__ é responsável por gerar 'ficheiros_destino' a partir do código-fonte, que podem ser usados por um utilizador final. Esses ficheiros podem ter a forma de bibliotecas, programas executáveis, scripts gerados, interfaces exportadas (por exemplo, arquivos de cabeçalho C ++) ou qualquer outra coisa que não seja um código estático. Na terminologia ROS, o código-fonte é organizado em 'pacotes', onde cada pacote normalmente consiste em um ou mais ficheiros quando compilado.

Para saber mais sobre o __catkin__ [consultar a página](https://wiki.ros.org/catkin/conceptual_overview).

## Instalação do "catkin"
O __catkin__ é incluído por defeito quando o ROS é instalado, embora também possa ser instalado a partir de pacotes fonte ou pré-compilados.

Por essa razão o ROS já deverá estra instalado quando se pretender criar um projeto.

Para saber mais sobre a instalação do __catkin__ consultar [esta](https://wiki.ros.org/catkin) página.


