## Odómetro

O [__"odometer"__ é um modulo ROS](../ROS/catkin_ws/src/utad_car_core/nodes/odometer), desenvolvido em Paython, cuja finalidade consiste em publicar a cada momento a velocidade linear e angular do __"utad_car"__ bem como a sua posição e orientação com base no movimento das rodas.

Este modo é composto por duas classes, a classe __"[Odometer](#Classe-Odometer)"__ e a classe __"[Encoder](#Classe-Encoder)"__.

A classe __"Encoder"__ é responsável pelo incremento ou decremento de um contador de impulsos para cada roda, dependendo do sentido de rotação do motor, enquanto que a classe __"Odometer"__ com base nos impulsos de cada roda, o numero de impulsos por rotação, o diâmetro das rodas e a distância entre rodas, calcula a posição do centro do carro e a sua orientação, bem como a respetiva velocidade linear e angular.

### Classe "Odometer"
A classe __Odometer__ utiliza para a realização dos seus cálculos os seguintes parâmetros:

        #Parameters
        self.rate = rospy.Rate(rospy.get_param('~rate', 1.0))
        self.distanceWheels = rospy.get_param('~wheel_base', 0.13)                #The distance between the wheels 
        self.wheelDiameter = rospy.get_param('~wheel_diameter', 0.067)            #Wheel diameter in meters
        self.ticksPerRevolution = rospy.get_param('~ticks_per_revolution', 20.0)  #Ticks per revolution

Esta classe publica no tópico __"odom"__ mensagens do tipo __"Odometry"__ baseadas na frame ID __"base_link"__.

Também publica no tópico __"odom/pose"__ mensagens do tipo __"geometry_msgs.msg.Pose2D"__.

Nesta classe ainda é subscrito o tópico __"reset"__ com mensagens do tipo __"Empty"__ que permite fazer o reset aos contadores de impulsos e á posição e velocidade do carro.

Note-se que esta função poderia ser facilmente modificada para em lugar de fazer o reset dos valores atribuir uma posição e velocidade ao carro caso se pretendesse.

### Classe "Encoder"

O __Encoder__ baseia-se na utilização de [rodas ranhuradas](./Roda%20ranhurada%20para%20odómetro.md) acopladas aos eixos dos motores que ao girarem ligam e desligam os [dispositivos de deteção de infravermelhos](./Detetor%20de%20velocidade%20por%20Infravermelhos.md), permitindo assim medir a rotação do motor.

Os impulsos gerados ao nível dos detetores de infravermelhos são encaminhados através dos pinos __GPIO__ do Raspberry PI, contabilizados nesta classe e utilizados para controlar a posição e a velocidade do __"utad_car"__.

A ativação das funcionalidades __GPIO__ no Raspberry PI com o sistema operativo __ubuntu 18.04__ está descrita [neste](./Controlo%20dos%20Motores%20de%20tração.md#configuração-do-sistema-operativo-para-aceder-às-ligações-i2c-spi-e-gpio) documento.

Os pinos utilizados para o controlo dos motores direito e esquerdo foram os seguintes:

        RW_TIC = 12             #Wheel right tick couter
        RW_DIR = 11             #Direction of the weel (1-forward else backard)
        LW_TIC = 36             #Wheel left tick couter
        LW_DIR = 35             #Direction of the weel (1-forward else backard)



