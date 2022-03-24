## Utilização da camara Raspberry PI

A utilização de camaras simples, como é o caso da [camara cedida pela UTAD](./Camera%205mp%200.575.md) permite através do tratamento adquado da imagem a movimentação de um robot, nomeadamente através do seguimento de marcas (veiculos filoguiados) e o seguimento de objetos móveis.

Para a utilização desta camara optei por adaptar os 'turtlebot3_autorace Packages' ao 'utad_car', seguindo as instruções da pǵina da ['ROBOTIS'](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#autonomous-driving), com a opção 'Noeic' e as devidas adaptações.

Como sugerido na página da 'ROBOTIS' o processamento é dividido entre o 'SBC' e um PC, que neste caso é substituido pelo 'Raspberry PI 4'

### Instalação no 'Raspberry PI 4'

Para suportar o processamento no 'Raspberry PI 4' criei os seguinte smodulos baseados no repositório [noetic-devel](https://github.com/ROBOTIS-GIT/turtlebot3_autorace_2020/tree/noetic-devel) :
 - utad_car_autorace_camera
 - utad_car_autorace_core
 - utad_car_autorace_detect
 - utad_car_autorace_driving
 - utad_car_autorace_msgs

Estes módulos permitem a recepção das imagens recolhidas no 'Raspberry PI 3' através da camera 'Raspberry PI', deteando as diferentes situações previstas e dando as convenientes instuções de movimentação ao 'utad_car'.

Depois de criados os modulos é necessário proceder á sua compilação e instalação dos modulos de tratamento de imagem, recorrendo aos seguintes comandos:

    cd ~/catkin_ws && catkin_make
    sudo apt install ros-noetic-image-transport ros-noetic-cv-bridge ros-noetic-vision-opencv python3-opencv libopencv-dev ros-noetic-image-proc

Para a instalação da camara 'Raspberry PI' no 'Raspberry PI 3' bem como os módulos ROS necessário, segui as instruções [desta página](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#autonomous-driving), utilizando os modulos o com as devidas adaptações.

Note-se que nesta página não existe código para o 'ROS Melodic' pelo que foram adaptados módulos do 'ROS Noetic' na instalação do 'Raspberry PI 3' e foi utilizado o 'Raspberry PI 4' como PC Remoto. 

Para estudar o comportamento desta camara começou-se pela [sua instalação](./Instalação%20da%20Camara%20Raspberry%20PI.md), seguindo para isso as instruções 

