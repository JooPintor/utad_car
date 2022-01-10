## Navegação básica do "utad_car"
O __utad_car__ com a [montagem básica](./Montagem%20do%20utad_car.md), tendo instalado no [Raspberry PI 3](./Raspberry%20PI%203.md) o __ububtu 18.04__ e o __ROS Melodic__ com o modulos [__motion__](./Controlo%20dos%20Motores%20de%20tração.md#modulo-motion) e [__odometer__](./Odómetro.md) já tem as condições minimas para poder mover-se, bastando para isso que se [publique no tópico __'cmd_vel'__](#Publicação-de-comandos-de-velocidade) uma mensagem com a velocidade pretendida.

Para utilização dos modulos básicos de navegação, deve-se [arrancar o modulo __'utad_car_core'__](#Arranque-do-modulo-utad_car_core), utilizando para isso o ficheiro [__'utad_car_core.launch'__](../ROS/catkin_ws/src/utad_car_core/launch/utad_car_core.launch).

Este ficheiro, alem de conter instruções de arranque dos modulos __motion__ e __odometer__, passa-lhes os seguintes valores:

  <node pkg="utad_car_core" type="motion" name="motion" output="$(arg output)">
      <param name="timeout" value="5" />
      <param name="rate" value="1.0" />
      <param name="max_speed" value="4095" />
      <param name="wheel_base" value="0.13" />
  </node>
  
  <node pkg="utad_car_core" type="odometer" name="odometer" output="$(arg output)">
      <param name="wheel_base" value="0.13" />
      <param name="wheel_diameter" value="0.066" />
      <param name="ticks_per_revolution" value="20.0" />
  </node>


### Arranque do modulo 'utad_car_core'

Para arrancar o modulo __'utad_car_core'__ deverão ser utilizados os seguintes comandos:

    source ~/catkin_ws/devel/setup.bash
    cd ~/catkin_ws
    roslaunch utad_car_core utad_car_core.launch

estes comandos estão disponíveis no ficheiro [__'utad_car_core.sh'__](../ROS/utad_car_core.sh) que poderá ser executado diretamente a partir da linha de comando.

### Publicação de comandos de velocidade
Uma forma fácil de enviar comandos de velocidade para o tópico __'cmd_vel'__ é recorrer ao modulo [__teleop_twist_keyboard__](../utils/teleop_twist/teleop_twist_keyboard.py) que é instalado com o __ROS__.

Para utilizar este modulo deverão ser utilizados os seguintes comandos:

    source ~/catkin_ws/devel/setup.bash
    cd ~/catkin_ws
    rosrun teleop_twist_keyboard teleop_twist_keyboard.py

Em alternativa podem ser utilizados __Scripts__ em Python para enviar mensagens para esse tópico, como é exemplificado nos seguintes scripts:
- [testMotors.py](../utils/TestScripts/testMotors.py) que envia um comando para o carro avançar.
- [testCarMoves.py](../utils/TestScripts/testCarMoves.py) que envia uma série de comandos que obrigam o carro a avançar, recuar, rodar sobre si mesmo, etc..
