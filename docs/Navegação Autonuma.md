## Navegação Autonuma

Por navegação autonoma, normalmente entende-se navegação sem intervenção humana.

A navegação Autonuma implica controlos a dois niveis:
  - __Baixo nível__, que inclui o controlo de velocidade, a deteção de colisões e obstaculos (eminente colisão)
  - __Alto nível__, que trata issencialmente os problemas da localização, mapeamento e planeamento de trajetórias
 
### Controlo de Bixo nível

O controlo de baixo nível é assegurado no __utad_car__ pelo modulo ROS [__motion__](./Controlo%20dos%20Motores%20de%20tração.md#modulo-motion), pela subscrição dos tópicos __'cmd_vel'__ e __'collision'__.

A patir do tópico __'cmd_vel'__ o modulo __motion__ consegue alterar a velocidade do carro (quer o valor da velocidade quer a direção), incluido a sua paragem (velocidade 0).

O modulo __motion__ na presença de uma mensagem no tópico __'collision'__ para de emediato os motores.
