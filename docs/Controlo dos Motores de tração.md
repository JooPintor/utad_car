## Controlo dos motores de tração
Para controlar a movimentação do robot "utad_car" foi utilizada a [placa de expanção do Raspberry PI](./Stepper%20Motor%20HAT%20for%20Raspberry%20Pi.md) fornecida pela Universidade.

Tratando-se de uma placa que comunica com o Raspberry PI por I2C foi necessário proceder [ativação da ligação por I2C no Raspberry PI](#configuração-do-raspberry-pi-para-arranque-das-ligações-por-i2c-e-spi) e á [configuração do acesso ao I2C no sistema operativo](#configuração-do-acesso-ao-i2c-no-sistema-operativo) antes de se poder enviar comandos para essa placa.



### Configuração do Raspberry PI para arranque das ligações por I2C e SPI
O Raspberry PI por defeito arranca sem as ligações I2C e SPI activas.

Para as activar é necessário configurar os ficheiros da area de "boot" para que no arranque do sistema essas ligações sejam consideradas.

O ficheiro em causa é o "/boot/firmware/syscfg.txt" qu epode ser editado com o seguinte comando:

    sudo nano /boot/firmware/syscfg.txt
    
Nesse ficheiro deverão ser acrescentadas se ainda não existitrem duas linhas seguintes:

    dtparam=i2c_arm=on
    dtparam=spi=on

A presença destas linhas neste ficheiro fazem com que o Raspberry arranque com estas ligações activas.


### Configuração do sistema operativo para aceder a I2C, SPI e GPIO.
Para que o sistema operativo possa comunicar com as ligações __I2C__, __SPI__ e com o pinos de ntradas e saidas __GPIO__, é necessário criar o seguite ficheiro "/etc/udev/rules.d/local.rules" com o comando:

    sudo nano /etc/udev/rules.d/local.rules

com o seguinte conteudo:

    ACTION=="add", KERNEL=="spidev0.*", GROUP="spi", MODE="0660"
    SUBSYSTEM=="bcm2835-gpiomem", KERNEL=="gpiomem", GROUP="gpio", MODE="0660"
    SUBSYSTEM=="gpio", KERNEL=="gpiochip*", ACTION=="add", PROGRAM="/bin/sh -c 'chown root:gpio /sys/class/gpio/export /sys/class/gpio/unexport ; chmod 220 /sys/class/gpio/export /sys/class/gpio/unexport'"
    SUBSYSTEM=="gpio", KERNEL=="gpio*", ACTION=="add", PROGRAM="/bin/sh -c 'chown root:gpio /sys%p/active_low /sys%p/direction /sys%p/edge /sys%p/value ; chmod 660 /sys%p/active_low /sys%p/direction /sys%p/edge /sys%p/value'"


Para permitir o acesso do sistema operativo á ligação I2C são necessárias diversa feramentas, nomeadamente "i2c-tools", "libi2c-dev" e "python3-smbus".


