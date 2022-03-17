## Controlo dos motores de tração
O "utad_car" trata-se de um carro robótico de duas rodas motrizes com motorização independente. 

Para controlar a movimentação do robot "utad_car" foi utilizado o [Raspberry PI 3](./Raspberry%20PI%203.md) e a [placa de expanção do Raspberry PI](./Stepper%20Motor%20HAT%20for%20Raspberry%20Pi.md) que a Universidade me forneceu para a realização do trabalho.

A placa de expansão que faz o controlo dos motores, trata-se de uma placa que comunica com o Raspberry PI por I2C, pelo que foi necessário proceder [ativação da ligação por I2C no Raspberry PI](#configuração-do-raspberry-pi-para-arranque-das-ligações-por-i2c-e-spi) e á [configuração do sistema operativo para aceder às ligações por I2C, SPI e GPIO](#Configuração-do-sistema-operativo-para-aceder-às-ligações-I2C-SPI-e-GPIO) de forma a preparar o Raspberry para comunicar com os periféricos, antes de se poder enviar comandos para alteração da velocidade de rotação dos motores e/ou poder ativar saídas e ler entradas nos seus pinos.

Para além das configurações já mencionadas, deverá proceder-se á [instalação de algumas ferramentas necessárias à ligação I2C](#instalação-de-ferramentas-necessárias-à-ligação-i2c), nomeadamente "i2c-tools", "libi2c-dev", "python3-dev" e "python3-smbus".

No final das configurações deverá ser feito um conjunto de [verificações](#Verificação-da-configuração) para nos assegurarmos que tudo ficou corretamente configurado.

Depois de configurado o Raspberry PI e o ubuntu para permitir as comunicações com a placa de expansão e com os pinos do Raspberry foi necessário criar as [classes em Python](#Classes-em-Python-para-controlo-dos-motores) constituintes do modulo ['motion'](#Modulo-motion), que permitem a interface com os motores a comunicação com outros módulos ROS.

### Configuração do Raspberry PI para arranque das ligações por I2C e SPI
O Raspberry PI por defeito arranca sem as ligações I2C e SPI ativas.

Para as ativar é necessário configurar os ficheiros da área de "boot" para que no arranque do sistema essas ligações sejam consideradas.

O ficheiro em causa é o "/boot/firmware/syscfg.txt" que pode ser editado com o seguinte comando:

    sudo nano /boot/firmware/syscfg.txt
    
Nesse ficheiro deverão ser acrescentadas se ainda não existirem duas linhas seguintes:

    dtparam=i2c_arm=on
    dtparam=spi=on

A presença destas linhas neste ficheiro faz com que o Raspberry arranque com estas ligações ativas.

### Configuração do sistema operativo para aceder às ligações I2C, SPI e GPIO 
Para que o utilizador (e as aplicações por ele executadas) possa ter acesso às ligações __I2C__, __SPI__ e aos pinos de entradas e saídas __GPIO__, será necessário [verificar a existência de grupos](#verificar-a-existencia-de-grupos) de utilizadores para cada tipo de ligação, [criar os grupos](#criação-de-grupos) que não existam e [incluir nos grupos o utilizador](#acrescentar-um-utilizador-a-um-grupo) que se pretenda vir a utilizar estas ligações, caso ainda não esteja incluído. A utilização das entradas/saídas GPIO requerem a utilização do grupo __kmem__.

Depois de verificada a inclusão do _utilizador_ nos grupos relevantes é necessária a [atribuição de permissões de acesso às ligações](#atribuição-de-permisões-às-ligações) aos grupos e [configurar o hardware das ligações](#Configuração-do-hardware-das-ligações-I2C-SPI-e-GPIO-no-sistema-operativo) para que este seja reconhecido pelo sistema operativo.

#### Verificar a existência de grupos
Para verificar a existência dos grupos que nos interessam deve-se realizar um comando para cada grupo como mostrado a seguir:

    getent group kmem
    getent group gpio
    getent group spi
    getent group i2c

A resposta a cada comando _getent_ caso o grupo exista consiste na lista de utilizadores que pertencem ao grupo.

No caso de não existir resposta é porque o grupo não existe e nesse caso é necessário criá-lo.

No caso de existir o grupo, mas o _utilizador_ não lhe pertencer deve-se acrescentar o _utilizador_ ao grupo.

#### Criação de grupos
Para a criação dos grupos poderão ser utilizados os seguintes comandos:

    sudo groupadd kmem
    sudo groupadd gpio
    sudo groupadd spi
    sudo groupadd i2c

#### Acrescentar um _utilizador_ a um grupo
Para acrescentar utilizadores aos grupos poderão ser utilizados os seguintes comandos:

    sudo usermod -a -G kmem "nome_do_utilizador"
    sudo usermod -a -G gpio "nome_do_utilizador"
    sudo usermod -a -G spi  "nome_do_utilizador"
    sudo usermod -a -G i2c  "nome_do_utilizador"

#### Atribuição de permissões às ligações
Para que o utilizador possa aceder às ligações é necessário dar permissões de acesso aos grupos criados

    sudo chgrp spi /dev/spidev0.0
    sudo chmod g+rw /dev/spidev0.0

    sudo chown root.gpio /dev/gpiomem
    sudo chmod g+rw /dev/gpiomem
    sudo chmod g+rw /dev/mem
    
    sudo chown :i2c /dev/i2c-1
    sudo chmod g+rw /dev/i2c-1

### Configuração do hardware das ligações I2C, SPI e GPIO no sistema operativo
Para que o sistema operativo possa comunicar com as ligações __I2C__, __SPI__ e com o pinos de entradas e saídas __GPIO__, é necessário copiar o ficheiro ['50-i2c-spi-gpio-udev.rules'](../ROS/50-i2c-spi-gpio-udev.rules) para a pasta __"/etc/udev/rules.d/"__ com o comando:

    sudo cp ./50-i2c-spi-gpio-udev.rules /etc/udev/rules.d/

Depois de ter copiado o ficheiro é necessário aplicar as novas regras executando o seguinte comando:

    sudo udevadm control --reload-rules && udevadm trigger

### Instalação de ferramentas necessárias à ligação I2C
Para facilitar a utilização da ligação I2C pelo ubuntu, deverão ser instalas as ferramentas seguintes, através da execução dos seguintes comandos:

    sudo apt-get update -y
    sudo apt-get install -y i2c-tools
    sudo apt-get install -y libi2c-dev
    sudo apt-get install -y python3-dev
    sudo -H pip3 install smbus
    sudo -H pip3 install smbus2
    sudo apt-get install -y python3-smbus
    
No caso do _"pip3"_ não estar instalado, deve proceder-se á sua instalação com o comando

    sudo apt install python-pip


### Verificação da configuração
Para verificar se todas as configurações estão corretas deverão ser executados os seguintes comandos e verificados os correspondentes resultados:

    ls -l /dev/spi*
    
    crw-rw---- 1 root spi 153, 0 ago 26 15:26 /dev/spidev0.0
    crw-rw---- 1 root spi 153, 1 ago 26 15:26 /dev/spidev0.1

    ls -l /dev/mem

    crw-rw---- 1 root kmem 1, 1 ago 26 15:26 /dev/mem

    ls -l /dev/gpiomem

    crw-rw---- 1 root gpio 239, 0 ago 26 15:26 /dev/gpiomem

    ls -l /dev/i2c*

    crw-rw---- 1 root i2c 89, 1 ago 26 15:26 /dev/i2c-1
    
    sudo i2cdetect -y 1

         0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 6f 
    70: 70 -- -- -- -- -- -- --     

    (Os valores retornados pelo comando "sudo i2cdetect -y 1" dependem do hardware ligado)

Notar as permissões de acesso "crw-rw----"  

### Classes em Python para controlo dos motores
As classes Python para controlo dos motores foram criadas a partir [destes exemplos](../utils/Raspi_MotorHAT/) de controlo disponíveis na Internet.

O modulo __'motion'__ baseia-se na classe __'motion_driver'__ que mantem dois objetos da classe __'Motor'__ (Motor\[LEFT] e Motor\[RIGHT]) que permitem controlar a velocidade dos motores DC.

Os objetos __'Motor'__ são obtidos pelo método __'getMotor()'__ da classe __'MotorHAT'__ que mantém as comunicações com a placa de expansão através da ligação I2C e o controlo de até 4 objetos da classe __'DCMotor'__.

Os objetos da classe __'DCMotor'__ permitem, com o método __'move()'__, a definição da velocidade do motor, através do ajuste do PWM da saída do respetivo motor e ainda a ativação de uma saída em função do sentido de rotação do motor, utilizando o método __'setPin()'__.

## Modulo 'motion'
O modulo ['motion'](../ROS/catkin_ws/src/utad_car_core/nodes/motion), alem de integrar as [classes de controlo dos motores](#Classes-em-Python-para-controlo-dos-motores), permite:  

- Subscrever as mensagens dos tópicos __'cmd_vel'__, __'collision'__ e __'odom'__ 
- Publicar mensagens no tópico __'cmd_vel'__

Neste modulo são recebidos comandos com valores de velocidade linear e angular pretendidas para o carro através do tópico __'cmd_vel'__, no formato __'Twist'__ que são utilizados para calcular as velocidades dos motores que lhes correspondem.

As velocidades dos motores são calculadas como uma percentagem da velocidade máxima do motor e estão limitadas a 100%.

Tendo em conta a não linearidade da relação entre a percentagem pedida e a percentagem obtida, em especial para percentagens baixas, foi introduzida uma correção ao valor a comandar baseada na medição da velocidade efetiva, recebida pelo tópico __'odom'__ com mensagens no formato __'Odometry'__. Estas mensagens são publicadas pelo [__Odómetro__](./Odómetro.md)

No caso da receção de uma mensagem de colisão pelo tópico __'collision'__ no formato __'String'__, a dizer _'obstacle_right'_ ou _'obstacle_left'_ os motores são parados.

Os motores também são parados se não forem recebidos comandos de velocidade durante um tempo superior ao definido em __'timeout'__. Este valor pode ser definido como parâmetro tendo por defeito o valor de 5 segundos.
