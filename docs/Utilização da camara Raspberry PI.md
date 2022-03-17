## Utilização da camara Raspberry PI

A utilização de camaras simples, como é o caso da [camara cedida pela UTAD](./Camera%205mp%200.575.md) permite através do tratamento adquado da imagem a movimentação de um robot, nomeadamente através do seguimento de marcas (veiculos filoguiados) e o seguimento de objetos móveis.

Para a utilização desta camara comecei por adaptar os 'turtlebot3_autorace Packages' ao 'utad_car' criado os seguintes módulos no 'Raspberry PI 4':
 - utad_car_autorace_camera
 - utad_car_autorace_core
 - utad_car_autorace_detect
 - utad_car_autorace_driving
 - utad_car_autorace_msgs

Para a utilização desta camara segui as instruções [desta página](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#autonomous-driving), com as devidas adaptações.

Note-se que nesta página não existe código para o 'ROS Melodic' pelo que foram adaptados módulos do 'ROS Noetic' na instalação do 'Raspberry PI 3' e foi utilizado o 'Raspberry PI 4' como PC Remoto.

Para estudar o comportamento desta camara começou-se pela [sua instalação](./Instalação%20da%20Camara%20Raspberry%20PI.md), seguindo para isso as instruções 

