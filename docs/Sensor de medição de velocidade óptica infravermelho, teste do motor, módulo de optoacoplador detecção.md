## Sensor de medição de velocidade óptica infravermelho, teste do motor, módulo de optoacoplador detecção

![image](https://user-images.githubusercontent.com/89998899/147965651-bcd112ef-96e4-49dd-997b-3ea124661b3f.png)

O sensor fotoelétrico tipo slot é composto por um infravermelho com uma ranhura de 5,9 mm. Contanto que o objeto não transparente passe pelo tipo de slot, ele pode ser acionado para emitir nível baixo de TTL. O gatilho Schmitt é usado para agitar o pulso, que é muito estável e pode ser usado para medir a velocidade do carro, medir distâncias e similares.

Tensão de trabalho: 3.3v-5v
Forma de saída: saída de interruptor digital (0 e 1)

Quando vcc e gnd são conectados, o indicador de sinal do módulo será ligado. Quando não há bloco no slot do módulo, o tubo de recepção é ligado e o módulo saída de alto nível. Ao bloquear, a saída de saída é baixa e o indicador de sinal está desligado. O módulo de saída pode ser conectado ao relé para formar um interruptor de limite e outras funções, e também pode ser conectado ao módulo de campainha ativa para formar um alarme. A interface de saída pode ser conectada diretamente à porta io do mcu. Geralmente, ele é conectado a uma interrupção externa para detectar se o sensor tem uma oclusão. Por exemplo, a roda de código do motor pode detectar a velocidade do motor.
