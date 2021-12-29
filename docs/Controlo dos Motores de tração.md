## Controlo dos motores de tração
Para controlar a movimentação do robot "utad_car" foi utilizada a [placa de expanção do Raspberry PI](./Stepper%20Motor%20HAT%20for%20Raspberry%20Pi.md) fornecida pela Universidade.

Tratando-se de uma placa que comunica com o Raspberry PI por I2C foi necessário proceder [ativação da ligação por I2C no Raspberry PI](#configuração-do-raspberry-pi-para-arranque-das-ligações-por-i2c-e-spi) e á [configuração do acesso ao I2C no sistema operativo](#configuração-do-acesso-ao-i2c-no-sistema-operativo) antes de se poder enviar comandos para essa placa.



### Configuração do Raspberry PI para arranque das ligações por I2C e SPI
O Raspberry PI por defeito arranca sem as ligações I2C e SPI activas.

Para as activar é necessário configurar os ficheiros da area de "boot" para que no arranque do sistema essas ligações sejam consideradas.

Para a alteração dos ficheiros em causa existe a ferramenta "raspi-config", no entanto, como essa ferramente não está disponivel no ubuntu, apesar de ser possível instala-la, opteio por editar na partição "system-boot" do cartão uSD o ficheiro "syscfg.txt", utilizando para isso outro PC, acrescentando-lhe as duas linhas seguintes:

    dtparam=i2c_arm=on
    dtparam=spi=on

A presença destas linhas neste ficheiro fazem com que o Raspberry arranque com estas ligações activas.


### Configuração do acesso ao I2C no sistema operativo

