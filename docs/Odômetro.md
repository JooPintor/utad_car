## Odômetro
O odômetro é um [modulo ROS](../ROS/catkin_ws/src/utad_car_core/nodes/odometer) cuja finalidade consiste em publicar a cada momento a velocidade linear e angular do __"utad_car"__.



O odômetro baseia-se na utilização de [rodas ranhuradas](./Roda%20ranhurada%20para%20odômetro.md) acopladas aos exos dos motores que ao girarem ligam e desligam os [dispositivos de deteção de infravermelhos](./Detetor%20de%20velocidade%20por%20Infravermelhos.md), permitindo assim medir a rotação do motor.

Os impulsos gerados ao nível dos detetores de ifra-vermelhos são encaminhados através dos pinos __GPIO__ do Raspbery PI e contabilizadoa no moódulo __'odometer'__ que controla a posição e a velocidade do __"utad_car"__.




