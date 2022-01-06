## Navegação básica do "utad_car"
O __utad_car__ com a [montagem básica](./Montagem%20do%20utad_car.md), tendo instalado no [Raspberry PI 3](./Raspberry%20PI%203.md) o __ububtu 18.04__ e o __ROS Melodic__ com o modulos [__motion__](./Controlo%20dos%20Motores%20de%20tração.md#modulo-motion) e [__odometer__](./Odómetro.md) já tem as condições minimas para poder mover-se, bastando para isso que se publique no tópico __'cmd_vel'__ uma mensagem com a velocidade pretendida.

Uma forma fácil de enviar comandos de velocidade para o tópico __'cmd_vel'__ é recorrer ao modulo [__teleop_twist_keyboard__](../utils/teleop_twist/teleop_twist_keyboard.py) que é instalado com o __ROS__.

Para utilizar este modulo deverão ser utilizados os seguintes comandos:
    source ~/catkin_ws/devel/setup.bash
    cd ~/catkin_ws
    rosrun teleop_twist_keyboard teleop_twist_keyboard.py
