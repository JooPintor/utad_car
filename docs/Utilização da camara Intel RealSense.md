## Utilização da camara Intel RealSense
A utilização de camaras com capacidade de captação de imagem e informação de profundidade, como é o caso da [Intel RealSense](./Camara%20Intel%20RealSense.md), apresenta-se como uma alternativa a considerar nos sistemas de navegação autónoma.

Esta camaras para além da deteção da distância aos obstáculos permitem a identificação de marcas estáticas no seu ambiente, localizando-se a partir das mesmas ou localizar elementos móveis, permitindo o estabelecimento de trajetórias em função da sua localização relativa.

Para estudar o comportamento desta camara começou-se pela [sua instalação](./Instalação%20da%20camara%20Intel%20RealSense.md).

A primeira instalação foi feita no Raspberry PI 3, onde tentei obter os dados necessários para alimentar o modulo de mapeamento e de deteção de obstáculos.

A visualização de imagens com a aplicação __realsense-viewer__ funciona relativamente bem, sendo possível visualizar tanto a _'Depth stream'_ como a _'Color stream'_, como mostra a imagem seguinte:

![realsense-viewer-rpi3](../imgs/realsense-viewer-rpi3.jpg)

No entanto quando se tenta obter imagens no ambiente ROS, utilizando o comando _roslaunch realsense2_camera rs_d435_camera_with_model.launch_ verifica-se que o mapeamento de pontos é muito deficiente apesar de estar com apenas 1 fps, como se pode observar na imagem seguinte:

![RViz-camera-model](../imgs/RViz-camera-model.jpg)

Ao mesmo tempo que se visualiza esta imagem, na janela onde foi executado o comando são continuamente apresentados os erros seguintes:

![erros-RViz-camera-model](../imgs/erros-RViz-camera-model.jpg)

Tendo em conta os resultados no _realsense-viewer_ e os resultados no _RViz_ admiti que uma das causas dos maus resultados e erros na utilização do _RViz_ poderia residir na falta de capacidade de processamento da imagem da camara ao mesmo tempo que é gerido o _ROS_ no _Raspberry PI 3_. Por esse motivo explorei a possibilidade de separar a captação da imagem e o controlo de baixo nível do controlo de alto nível, instalando o ROS em dois locais, com processamento independente e comunicação pela rede LAN.

Foram assim estudadas as seguintes hipóteses de locais de processamento, admitindo que a captação de imagens se faria sempre ao nível do _Raspberry PI 3_:
- [Raspberry PI 4](#Processamento-no-Raspberry-PI-4)
- [PC Portatil](#Processamento-da-Imagem-no-PC-Portatil)
- [Carta Nvidia Jetson Nano](#Processamento-da-Imagem-na-Carta-Nvidia-Jetson-Nano)

Para utilizar outro local de processamento de alto nível é necessário ai arrancar com o _ROS_  como 'Master', sendo os módulos de baixo nível executados no _Raspberry PI 3_ com a indicação do endereço do 'Master'.

### Processamento no Raspberry PI 4

Para utilizar o _Raspberry PI 4_ como local de processamento de alto nível comecei por testar o modulo _realsense2_camera_ utilizando para o efeito o script [rpi4_rs2_camera.sh](../ROS/rpi4_rs2_camera.sh), e utilizando em particular os seguintes comandos:

      export ROS_MASTER_URI=http://rpi4.local:11311

      source ~/catkin_ws/devel/setup.bash
      cd ~/catkin_ws

      roslaunch realsense2_camera rs_camera.launch enable_sync:=true



### Processamento da Imagem no PC Portatil

### Processamento da Imagem na Carta Nvidia Jetson Nano

Como explicado no [modulo de instalação](../docs/Instalação%20da%20camara%20Intel%20RealSense.md#instalação-do-sdk-da-camara) da camara na __carta Nvidia Jetson Nano__ tendo em conta as dificuldades encontradas na instalação dos drivers da camara nessa placa acabei por abandonar a hipótese de utilização dessa carta para o processamento da imagem obtida no Raspberry PI 3.
