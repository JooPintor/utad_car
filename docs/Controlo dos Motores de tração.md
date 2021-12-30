## Controlo dos motores de tração
O "utad_car" trata-se de um carro robotico de duas rodas motrizes com motorização independente. 

Para controlar a movimentação do robot "utad_car" foi utilizado o [Raspberry PI 3](./Raspberry%20PI%203.md) e a [placa de expanção do Raspberry PI](./Stepper%20Motor%20HAT%20for%20Raspberry%20Pi.md) que a Universidade me forneceu para a realização do trabalho.

A placa de expansão que faz o controlo dos motores, tratando-se de uma placa que comunica com o Raspberry PI por I2C, pelo que foi necessário proceder [ativação da ligação por I2C no Raspberry PI](#configuração-do-raspberry-pi-para-arranque-das-ligações-por-i2c-e-spi) e á [configuração do sistema operativo para aceder às ligaçõe por I2C, SPI e GPIO](#Configuração-do-sistema-operativo-para-aceder-às-ligações-I2C-SPI-e-GPIO) antes de se poder enviar comandos para essa placa ou poder activar saídas e ler entradas nos pinos do Raspberry.

Em simultâneo com a configuração da ligação I2C pode-se fazer a [configuração das ligações SPI e GPIO](#Configuração-do-sistema-operativo-para-aceder-as-ligações-SPI-e-GPIO), já que envolvem acções semelhantes e também são necessárias para o controlo.

Para além das configurações já mensionadas, deverá proceder-se á [instalação de algumas feramentas necessárias à ligação I2C](#instalação-de-ferramentas-necessárias-à-ligação-i2c), nomeadamente "i2c-tools", "libi2c-dev", "python3-dev" e "python3-smbus".

No final das convigurações deverá ser feito um conjunto de [verificações](#Verificação-da-configuração) para nos acegurar-mos que tudo ficou corretamente configurado- 

### Configuração do Raspberry PI para arranque das ligações por I2C e SPI
O Raspberry PI por defeito arranca sem as ligações I2C e SPI activas.

Para as activar é necessário configurar os ficheiros da area de "boot" para que no arranque do sistema essas ligações sejam consideradas.

O ficheiro em causa é o "/boot/firmware/syscfg.txt" que pode ser editado com o seguinte comando:

    sudo nano /boot/firmware/syscfg.txt
    
Nesse ficheiro deverão ser acrescentadas se ainda não existitrem duas linhas seguintes:

    dtparam=i2c_arm=on
    dtparam=spi=on

A presença destas linhas neste ficheiro fazem com que o Raspberry arranque com estas ligações activas.


### Configuração do sistema operativo para aceder às ligações I2C, SPI e GPIO 
Para que o utilizador (e as aplicações por ele executadas) possa ter acesso ás ligações __I2C__, __SPI__ e aos pinos de ntradas e saidas __GPIO__, será necessário [verificar a existencia de grupos](#verificar-a-existencia-de-grupos) de utilizadores para cada tipo de ligação, [criar os grupos](#criação-de-grupos) que não existam e [incluir no grupo o utilizador](#acrescentar-um-utilizador-a-um-grupo) que se pretenda vir a utilizar estas ligaçoes, caso ainda não esteja incluido. A utilização das entradas/saidas GPIO requerem a utilização do grupo _kmem_.

Depois de verificada a iclusão do _utilizador_ nos grupos relevantes é necessária a [atribuição de permisões de acesso ás ligações](#atribuição-de-permisões-ás-ligações) aos gropos.

#### Verificar a existencia de grupos
Para verificar a existencia dos grupos que nos interessam deve-se realizar um comando para cada grupo como mostrado a seguir:

    getent group kmem
    getent group gpio
    getent group spi
    getent group i2c

A resposta a cada comando _getent_ caso o grupo exista consiste na lista de utilizadores que pertencem ao grupo.

No caso de não existir resposta é porque o grupo não existe e nesse caso é necessário cria-lo.

No caso de existir o grupo mas o _utilizador_ não lhe pertencer deve-se acrescentar o _utilizador_ ao grupo.

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

#### Atribuição de permisões ás ligações
Para que o utilizador possa aceder ás ligações é necessário dar permições de acesso aos grupos criados

    sudo chgrp spi /dev/spidev0.0
    sudo chmod g+rw /dev/spidev0.0

    sudo chown root.gpio /dev/gpiomem
    sudo chmod g+rw /dev/gpiomem
    sudo chmod g+rw /dev/mem
    
    sudo chown :i2c /dev/i2c-1
    sudo chmod g+rw /dev/i2c-1

#### Instalação de ferramentas necessárias à ligação I2C
Para facilitar a utilização da ligação I2C pelo ubuntu, deverão ser instalas as ferramentas seguintes, através da execução dos seguintes comandos:

    sudo apt-get update -y
    sudo apt-get install -y i2c-tools
    sudo apt-get install -y libi2c-dev
    sudo apt-get install -y python3-dev
    sudo -H pip3 install smbus
    sudo -H pip3 install smbus2
    sudo apt-get install -y python3-smbus
    
No caso do _pip3_ não estar instalado, deve proceder-se á sua instalação com o comando

    sudo apt install python-pip

### Configuração do sistema operativo para aceder às ligações SPI e GPIO
Para que o sistema operativo possa comunicar com as ligações __SPI__ e com o pinos de ntradas e saidas __GPIO__, é necessário criar o ficheiro "/etc/udev/rules.d/local.rules" com o comando:

    sudo nano /etc/udev/rules.d/local.rules

com o seguinte conteudo:

    ACTION=="add", KERNEL=="spidev0.*", GROUP="spi", MODE="0660"
    SUBSYSTEM=="bcm2835-gpiomem", KERNEL=="gpiomem", GROUP="gpio", MODE="0660"
    SUBSYSTEM=="gpio", KERNEL=="gpiochip*", ACTION=="add", PROGRAM="/bin/sh -c 'chown root:gpio /sys/class/gpio/export /sys/class/gpio/unexport ; chmod 220 /sys/class/gpio/export /sys/class/gpio/unexport'"
    SUBSYSTEM=="gpio", KERNEL=="gpio*", ACTION=="add", PROGRAM="/bin/sh -c 'chown root:gpio /sys%p/active_low /sys%p/direction /sys%p/edge /sys%p/value ; chmod 660 /sys%p/active_low /sys%p/direction /sys%p/edge /sys%p/value'"


### Verificação da configuração
Para verificar se todas as configurações estão corretas deverão ser executados os seguintes comando e verificados os correspondentes resultados:

    ls -l /dev/spi*
    
    crw-rw---- 1 root spi 153, 0 ago 26 15:26 /dev/spidev0.0
    crw-rw---- 1 root spi 153, 1 ago 26 15:26 /dev/spidev0.1

    ls -l /dev/mem

    crw-r----- 1 root kmem 1, 1 ago 26 15:26 /dev/mem

    ls -l /dev/gpiomem

    crw-rw---- 1 root gpio 239, 0 ago 26 15:26 /dev/gpiomem

    cat /etc/udev/rules.d/local.rules

    ACTION=="add", KERNEL=="spidev0.*", GROUP="spi", MODE="0660"
    SUBSYSTEM=="bcm2835-gpiomem", KERNEL=="gpiomem", GROUP="gpio", MODE="0660"
    SUBSYSTEM=="gpio", KERNEL=="gpiochip*", ACTION=="add", PROGRAM="/bin/sh -c 'chown root:gpio /sys/class/gpio/export /sys/class/gpio/unexport ; chmod 220 /sys/class/gpio/export /sys/class/gpio/unexport'"
    SUBSYSTEM=="gpio", KERNEL=="gpio*", ACTION=="add", PROGRAM="/bin/sh -c 'chown root:gpio /sys%p/active_low /sys%p/direction /sys%p/edge /sys%p/value ; chmod 660 /sys%p/active_low /sys%p/direction /sys%p/edge /sys%p/value'"

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


