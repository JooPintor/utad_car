## Controlo dos motores de tração
Para controlar a movimentação do robot "utad_car" foi utilizada a [placa de expanção do Raspberry PI](./Stepper%20Motor%20HAT%20for%20Raspberry%20Pi.md) fornecida pela Universidade.

Tratando-se de uma placa que comunica com o Raspberry PI por I2C foi necessário proceder [ativação da ligação por I2C no Raspberry PI](#configuração-do-raspberry-pi-para-arranque-das-ligações-por-i2c-e-spi) e á [configuração do acesso ao I2C no sistema operativo](#configuração-do-acesso-ao-i2c-no-sistema-operativo) antes de se poder enviar comandos para essa placa.



### Configuração do Raspberry PI para arranque das ligações por I2C e SPI
O Raspberry PI por defeito arranca sem as ligações I2C e SPI activas.

Para as activar é necessário configurar os ficheiros da area de "boot" para que no arranque do sistema essas ligações sejam consideradas.

O ficheiro em causa é o "/boot/firmware/syscfg.txt" que pode ser editado com o seguinte comando:

    sudo nano /boot/firmware/syscfg.txt
    
Nesse ficheiro deverão ser acrescentadas se ainda não existitrem duas linhas seguintes:

    dtparam=i2c_arm=on
    dtparam=spi=on

A presença destas linhas neste ficheiro fazem com que o Raspberry arranque com estas ligações activas.


### Configuração do sistema operativo para aceder aa ligações I2C, SPI e GPIO.
Para que o sistema operativo possa comunicar com as ligações __I2C__, __SPI__ e com o pinos de ntradas e saidas __GPIO__, é necessário criar o ficheiro "/etc/udev/rules.d/local.rules" com o comando:

    sudo nano /etc/udev/rules.d/local.rules

com o seguinte conteudo:

    ACTION=="add", KERNEL=="spidev0.*", GROUP="spi", MODE="0660"
    SUBSYSTEM=="bcm2835-gpiomem", KERNEL=="gpiomem", GROUP="gpio", MODE="0660"
    SUBSYSTEM=="gpio", KERNEL=="gpiochip*", ACTION=="add", PROGRAM="/bin/sh -c 'chown root:gpio /sys/class/gpio/export /sys/class/gpio/unexport ; chmod 220 /sys/class/gpio/export /sys/class/gpio/unexport'"
    SUBSYSTEM=="gpio", KERNEL=="gpio*", ACTION=="add", PROGRAM="/bin/sh -c 'chown root:gpio /sys%p/active_low /sys%p/direction /sys%p/edge /sys%p/value ; chmod 660 /sys%p/active_low /sys%p/direction /sys%p/edge /sys%p/value'"

### Configuração do utilizador para aceder aa ligações I2C, SPI e GPIO 
Para que o utilizador (e as aplicações por ele executadas) possa ter acesso ás ligações __I2C__, __SPI__ e aos pinos de ntradas e saidas __GPIO__, será necessário verificar a existencia de grupos de utilizadores para cada tipo de ligação, crialos caso não existam e incluir nos mesmo o utilizador que se pretenda vir a utilizar estas ligaçoes.

#### Verificar a existencia de grupos
Para verificar a existencia dos grupos que nos interessam deve-se realizar um comando para cada grupo como mostrado a seguir:

    getent group kmem
    getent group gpio
    getent group spi
    getent group i2c

A resposta a cada comando _getent_ caso o grupo exista consiste na lista de utilizadores que pertencem ao grupo.

No caso de não existir resposta é porque o grupo não existe e nesse caso é necessário cria-lo.

No caso de existir o grupo mas o _utilizador_ não lhe pertencer deve-se acrescentar o _utilizador_ ao grupo.

#### Criação de um grupo
Para a criação dos grupos poderão ser utilizados os seguintes comandos:

    sudo groupadd kmem
    sudo groupadd gpio
    sudo groupadd spi
    sudo groupadd i2c

#### Acrescentar um _utilizador_ a um grupo
Para acrescentar utilizadores aos grupos poderão ser utilizados os seguintes comandos:

    sudo usermod -a -G kmem "nome_do_utilizador"
    sudo usermod -a -G gpio "nome_do_utilizador"
    sudo usermod -a -G spi "nome_do_utilizador"
    sudo usermod -a -G i2c "nome_do_utilizador"
    


Para permitir o acesso do sistema operativo á ligação I2C são necessárias diversa feramentas, nomeadamente "i2c-tools", "libi2c-dev" e "python3-smbus".


