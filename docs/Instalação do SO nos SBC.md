## Instalação do SO nos SBC
Um computador de placa única (SBC - Single Board Computer) é um computador inteiro construído numa só placa de circuito impresso.
Os SBCs vêm completos com memória, um microprocessador, entradas e saídas.

Embora o Raspberry Pi esteja entre os PCs de placa única mais populares e versáteis, está longe de ser a única opção.

A maioria dos SBCs executa bem os sistemas operativos Linux. No entanto, alguns oferecem compatibilidade com Android e Chrome OS.

Normalmente são criadas comunidades de utilizadores que desenvolvem sistemas operativos e aplicações para os SBCs criando versões de SOs que tiram partido das características de cada SBC, mas também existem comunidades de utilizadores que desenvolvem SOs independentes dos SBCs em utilização.

São exemplos a Raspberry que criou o SO Raspbian para os seus SBCs (rpi3 e rpi4) e a Canonical que desenvolve o SO Ubuntu que pode ser instalado tanto em PCs como SBCs de diferentes fabricantes.

Tendo em conta que o ROS foi originalmente desenvolviso para o sistema Linux, a minha opção vai para a instalação deste SO e em particular as versões Ubuntu 18.04 LTS e Ubuntu 20.04 LTS por serem as que têm mais suporte da comunidade de utilizadores do ROS. Também cheguei a instalar o Raspbian, no entanto neste SO foi necessário compilar o ROS a partir do código fonte.

Na seleção do SO a instalar no SBC para alem da escolha da opção Linux tem que se ter em conta a arquitetura do processador do SBC. No caso dos SBCs com arquitetura ARM (ARM - Advanced RISC Machines)(RISC - Reduced Instruction Set Computer) deve-se ter ainda o cuidado de garantir que a versão do SO é compatível com o numero de bits do processador e com a memória RAM disponível no SBC.

As arquiteturas dos SBCs testados foram as seguintes:
- O Raspberry Pi 3 - processador ARMv7 com arquitetura ARM de 32 bits ARMhf (com suporte de virgula flotuante por hardware)
- O Raspberry Pi 4 - processador ARMv8 com arquitetura ARM de 64 bits ARM64.
- Nvidia Jetson Nano - processador ARMv8 com arquitetura ARM de 64 bits ARM64

No caso dos SBCs testados o sitema opertivo arranca a partir de um cartão uSD que funciona como "disco" do sistema tendo sido utilizados cartões com o minimo de 16 GB, apesar de ser possível instalar o sistema com cartões de apenas 8 GB.

Para a instalação dos sistemas nos SBCs deve-se começar por criar a imagem de um disco com capacidade de arranque (com informação de arranque nos primeiros sectores do disco) e que contenha a informação minima para a configuração do sistema.

Em alternativa pode-se criar uma imagem de um sistema já instalado num SBC semelhante.

Existem diversos softwares de criação decópia de imagens para cartões SD sendo os mais utilizados os seguintes:
- [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
- [balenaEtcher](https://www.balena.io/etcher/)

Para a realização do trabalho foi testada a instalação de diversa imagens de SOs, nomeadamente as seguintes:
- [ubuntu-18.04.5-preinstalled-server-armhf+raspi3.img.xz](https://cdimage.ubuntu.com/releases/18.04/release/)
- [ubuntu-20.04.3-preinstalled-server-arm64+raspi.img.xz](https://cdimage.ubuntu.com/releases/20.04/release/)
- [ubuntu-18.04.2-beta2-desktop-armhf+raspi-ext4.img.xz](https://releases.ubuntu-mate.org/archived/18.04/armhf/)
- [ububtu-mate-20.04.1-desktop-armhf+raspi.img.xz](https://releases.ubuntu-mate.org/20.04/armhf/)
- [ubuntu-20.04.3-live-server-arm64.iso](https://cdimage.ubuntu.com/releases/20.04/release/)
- [2021-05-07-raspios-buster-armhf-full.zip](https://linuxdistros.org/torrents/raspios-2021-05-07-buster-armhf.zip.html)
- [2021-05-07-raspios-buster-arm64.zip](http://ftp.jaist.ac.jp/pub/raspberrypi/raspios_arm64/images/raspios_arm64-2021-05-28/)
- [jetson-nano-2gb-jp451-sd-card-image.zip](https://developer.nvidia.com/embedded/downloads#?search=jetson-nano-2gb-sd-)
- [ros-melodic-arm-2021-02-01.img.tar.gz](https://husarion.com/downloads/)
- [ros-noetic-arm-2021-02-01.img.tar.gz](https://husarion.com/downloads/)
- [ ros4raspbian-melodic-armhf-1.0.0.zip](https://github.com/nomumu/ros4raspbian/releases)

Com o cartão SD com a imagem pretendida gravada deve proceder-se á preparação do cartão para o primeiro arranque do SBC com o mesmo.

No caso das imagens para a instalação do sistema desde o início, não são necessárias preparações já que todos os dados de configuração vão sendo solicitados durante o processo de instalação.

No caso de imagens pré-instaladas é necessário saber o nome de utilizador e a palavra passe utilizadas na pré-instalação.

Em particular nas situações em que não esteja disponível uma ligação por cabo ao SBC há necessidade de [configurar o acesso á rede LAN](#configuração-do-acesso-á-rede-lan) a que o SBC se poderá ligar quando arrancar.

### Instalação do "desktop"
Nas opções de imagens apenas servidores é ainda conveniente instalar um “desktop” para permitir o interface gráfico com o sistema.

Sugiro a instalação do desktop “lubuntu” por se tratar de um desktop simples, mas com tudo o que necessitamos para a utilização pretendida.

Para a instalação do desktop deverão ser executados os seguintes comandos numa janela de comandos do servidor:

    sudo apt update
    sudo apt install lubuntu-desktop
    sudo reboot

Para se tirar partido do interface gráfico do "desktop" nos acessos ao SBC a partir de um PC, pode-se optar pela [instalação de um servidor RDP](#instalação-de-um-servidor-rdp) o que permitirá aceder ao desktop através da interface gráfica. 

Nas versões pré-instaladas, por razões de segurança ou outras pode ser desejável a troca do [nome do utilizador](#alteração-do-username-em-sistemas-linux) e da [palavra passe](#alteração-da-password-em-sistemas-linux), bem como do [nome do SBC na rede](#alteração-do-hostname-em-sistemas-linux).

Essas alterações podem ser feitas seguindo estas instruções.

### Instalação de um servidor RDP
O pacote Xrdp está disponível nos repositórios padrão do Linux. Para instalá-lo basta executar os seguintes comandos:

	sudo apt update
	sudo apt install xrdp
	sudo adduser xrdp ssl-cert


### Configuração do acesso á rede LAN 
Com o cartão SD inserido no PC, na partição de “system-boot” do cartão, que contém arquivos de configuração inicial que são carregados durante o primeiro processo de inicialização, devemos editar o ficheiro “network-config” , introduzindo as credenciais de acesso á rede WiFi e o modo de ligação, se com endereço obtido por DHCH ou se com endereço fixo.

Para fazer isso, deve-se descomentar (remover o “#” no início da linha) e editar as seguintes linhas:

    wifis:
      wlan0:
        dhcp4: true
        optional: true
        access-points:
          <wifi network name>:
            password: "<wifi password>"

Por exemplo:

    wifis:
      wlan0:
        dhcp4: true
        optional: true
        access-points:
          "home network":
            password: "123456789"

Nota: o nome da rede deve ser colocado entre aspas.

O exemplo de configuração corresponde á opção de obtenção de endereço por DHCP, para configurar um endereço de IP fixo podem-se seguir as seguintes instruções:

__Definição de um IP estático__

Para definir um IP estático, é necessário substituir no arquivo de configuração de rede a linha

    dhcp4: true

por linhas que especificam o endereço IP pretendido,  o gateway padrão e o servidor DNS.

Esta configuração pode ser feita para a interface __eth0__ ou __wlan0__ (ou ambas).

__É importante utilizar o “ident” correto para que a configuração seja reconhecida__

Exemplo:

    ethernets:
      eth0:
        addresses:
          - 192.168.101.23/24
        gateway4: 192.168.1.1
        nameservers:
          addresses: [192.168.1.23]
        optional: true 

### Alteração do “username” em sistemas Linux
Para alterar o nome de um utilizador esse utilizador não poderá estar ativo no sistema, pelo que se deverá começar por atribuir password ao utilizador “root” e arrancar a cessão com esse utilizador

    sudo passwd root
    sudo reboot

Fazendo login com a conta "root" e a senha definida anteriormente alterar nome de utilizador e a pasta pessoal para o novo nome desejado.

    usermod -l <novonome> -d /home/<novonome> -m <velhonome>
	groupmod -n <novonome> <velhonome>
    passwd -l root
    exit

Nota: Em SBCs que apenas estejam acessiveis por SSH (não estejam ligados com teclado e monitor) poderá ser necessário alterar a [configuração do servidor SSH](#configuração-do-servidor-ssh-para-permitir-o-login-do-root) para permitir o login do utilizador "root"  

### Alteração da “password” em sistemas Linux
Algumas imagens obrigam á alteração da palavra passe durantre a primeira inicialização.

No caso das imagens em que tal não ocorre ou por qualquer outra razão, a palavra passe de um sitema Linux pode a qualquer momento ser alterada utilizando o comando seguinte:

    passwd

### Alteração do “hostname” em sistemas Linux
Digitar o seguinte comando para editar "/etc/hostname" utilizando o editor de texto nano:

    sudo nano /etc/hostname

Neste ficheiro deve-se substituir o antigo nome pelo novo nome.

De seguida, deve-se editar também o ficheiro "/etc/hosts" com o comando:

    sudo nano /etc/hosts

Neste ficheiro deverá ser substituida qualquer ocorrência do antigo nome pelo novo nome.

As alterações terão efeito no proximo arranque do sistema:

    sudo reboot

### Configuração do servidor SSH para permitir o "login" do "root"
Para habilitar o login via SSH ao utilizador root num sistema Debian Linux, é necessário primeiro configurar o servidor SSH.

Para isso é necessário editar o ficheiro "/etc/ssh/sshd_config"

	sudo nano /etc/ssh/sshd_config

Neste ficheiro deverá ser alterada a seguinte linha:

	De:
	PermitRootLogin without-password
	
	Para:
	PermitRootLogin yes
	
Depois de feita a alteração acima, deve-se reiniciar o servidor SSH:

	sudo /etc/init.d/ssh restart
	
__Nota importante: Logo que não seja necessário o login do root por SSH o mesmo deve ser desabilitado por razões de segurança, repondo a configuração por defeito__



