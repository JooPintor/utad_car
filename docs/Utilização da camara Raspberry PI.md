## Utilização da camara Raspberry PI

A utilização de camaras simples, como é o caso da [camara cedida pela UTAD](./Camera%205mp%200.575.md) permite através do tratamento adequado da imagem a movimentação de um robot, nomeadamente através do seguimento de marcas (veículos filo guiados) e o seguimento de objetos móveis.

Para a utilização desta camara optei por adaptar os 'turtlebot3_autorace Packages' ao 'utad_car', seguindo as instruções da página da ['ROBOTIS'](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#autonomous-driving), opção 'Noetic' e as devidas adaptações.

Como sugerido na página da 'ROBOTIS' o processamento é dividido entre o 'SBC' e um PC, que neste caso é substituído pelo 'Raspberry PI 4'

### Instalação no 'Raspberry PI 4'

Para suportar o processamento no 'Raspberry PI 4' criei os seguintes módulos baseados no repositório [noetic-devel](https://github.com/ROBOTIS-GIT/turtlebot3_autorace_2020/tree/noetic-devel) :
 - utad_car_autorace_camera
 - utad_car_autorace_core
 - utad_car_autorace_detect
 - utad_car_autorace_driving
 - utad_car_autorace_msgs

Estes módulos permitem a recepção das imagens recolhidas no 'Raspberry PI 3' através da camara 'Raspberry PI', detetando as diferentes situações previstas e dando as convenientes instruções de movimentação ao 'utad_car'.

Depois de criados os módulos é necessário proceder á sua compilação e instalação dos módulos de tratamento de imagem, recorrendo aos seguintes comandos:

    cd ~/catkin_ws && catkin_make
    sudo apt install ros-noetic-image-transport ros-noetic-cv-bridge ros-noetic-vision-opencv python3-opencv libopencv-dev ros-noetic-image-proc

### Instalação no 'Raspberry PI 3'

Subdividi a instalação no 'Raspberry PI 3' em duas partes, a instalação da camara e a instalação dos módulos ROS que permitem a ligação da camara ao ROS.

#### Instalação da camara 'Raspberry PI' no SBC

A instalação da camara 'Raspberry PI' no 'Raspberry PI 3' baseou-se nas instruções da página da 'ROBOTIS', a partir da qual preparei [estas instruções](./Instalação%20da%20Camara%20Raspberry%20PI.md).

#### Instalação dos modulos 'ROS' no 'SBC'

Para a instalação dos modulos'ROS' no 'Raspberry PI 3' foi necessário criar um conjunto de modulos semelhantes aos criados no 'Raspberry PI 4', neste caso baseados no no repositório [feature-raspicam](https://github.com/ROBOTIS-GIT/turtlebot3_autorace_2020/tree/feature-raspicam).

Note-se que embora exista [código](https://github.com/ROBOTIS-GIT/turtlebot3_autorace/tree/melodic-devel) para o 'ROS Melodic' foram adaptados os módulos do 'ROS Noetic', já que a versão para o para o 'ROS Melodic' é antiga. 

### Calibração da camara
Calibrar a câmara é muito importante para a navegação autônoma. Os passos necessários à calibração da câmara de forma simples, são descritos a seguir.

#### Verificação da imagem da câmara
Para a verificação da imagem da câmara devem-se executar os seguintes paços:

- No 'Raspberry PI 4' executar o comando:

        roscore
  
- No 'Raspberry PI 3' executar o comando:

        roslaunch utad_car_autorace_camera raspberry_pi_camera_publish.launch 
  
- No 'Raspberry PI 4' executar o comando:

        rqt_image_view
  
Após a execução deste comando deverá ser possível visualizar no 'Raspberry PI 4' a imagem captada pela câmara ligada ao 'Raspberry PI 3'
