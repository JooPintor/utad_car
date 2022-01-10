## Navegação Autónoma

Por navegação autónoma, normalmente entende-se navegação sem intervenção humana.

A navegação Autónoma implica controlos a dois níveis:
  - __Baixo nível__, que inclui o controlo de velocidade, a deteção de colisões e obstáculos (eminente colisão)
  - __Alto nível__, que trata essencialmente os problemas da localização, mapeamento e planeamento de trajetórias
 
### Controlo de Baixo nível

O controlo de baixo nível é assegurado no __utad_car__ pelo modulo ROS [__motion__](./Controlo%20dos%20Motores%20de%20tração.md#modulo-motion), pela subscrição dos tópicos __'cmd_vel'__ e __'collision'__.

A partir do tópico __'cmd_vel'__ o modulo __motion__ consegue alterar a velocidade do carro (quer o valor da velocidade quer a direção), incluindo a sua paragem (velocidade 0).

O modulo __motion__ na presença de uma mensagem no tópico __'collision'__ para de imediato os motores.

### Controlo de Alto nível

Para o controlo de alto nivel o primeiro problema a tratar prede-se com a determinação da sua localização num plano 2D.

O modulo [__odometer__](./Odómetro.md), incluído no controlo de baixo nível, permite ainda que de forma grosseira ter alguma informação sobre as coordenadas do carro num plano 2D.

No entanto para a navegação autónoma é necessário ainda tratar da deteção de obstáculos e o mapeamento do ambiente para se poderem planear trajetórias.

A utilização de mapas permite ajustar a localização, em particular se forem utilizados referenciais que possam ser identificados em imagens.

Para a execução de mapas foram abordados dois métodos:
- Recurso a um dispositivo LIDAR
- Recurso á camara Intel Realsense II

Tendo em conta que a [__Robotis__](http://en.robotis.com/) disponibiliza soluções de navegação para o seu [__TurtleBot3__](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/#overview), que se trata de um carro robótico baseado num SBCs __Raspberry PI__ com SO __ubuntu__ e também com tração a duas rodas, adaptei o codigo do __TurtleBot3__ ao __utad_car__, tendo em conta as diferenças existentes no controlo a baixo nível.

Dessa forma foram criados grande parte dos modulos ROS para o contolo de alto nível do 'utad_car' [aqui disponíveis](../ROS/catkin_ws/src/).

O estudo da navegação a este nivel centrou-se no [recurso a SLAM](./SLAM.md) e á [utilização da camara Intel Real Sense](), por terem sido os dispositivos disponibilizados pela Universidade para a realização dos estudos. 

