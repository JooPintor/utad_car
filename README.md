# tese
Esta pagina tem o objectivo de ser um depositorio de conhecimento para o ensino de utilização de ROS e introdução de visão a robos, os sucessus e fracasso enquanto á sua utilização e emplemtação com o material utilizado listado nas alinhas a seguir.

- O que é ROS?\n
Robot Operating System é o sistema mais utilizados nos ultimos anos quando se vem há robotica, sendo este uma framework crianda a partir da ligação de diferentes computadores que assim vai criar o seu proprio sistema operativo para o robo que está a ser programado, para comprir as suas funções.

- Material utilizado
Rasperry Pi 3: Ubuntu Rob3: Linux verº18.04: ROS-melodic:
SBC (Single Board Computers)
 
Raspberry PI 3
cat /proc/cpuinfo
 
Processors: 4
model name      : ARMv7 Processor rev 4 (v7l)
BogoMIPS           : 57.60
Features              : half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm crc32
CPU implementer            : 0x41
CPU architecture: 7
CPU variant        : 0x0
CPU part             : 0xd03
CPU revision       : 4
 
Hardware            : BCM2835
Revision              : a02082
Serial                    : 00000000b0efcb08
Model                  : Raspberry Pi 3 Model B Rev 1.2
 
cat /proc/meminfo
MemTotal: 876176 kB
 
OS:
cat /etc/os-release
 
NAME="Ubuntu"
VERSION="18.04.6 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.6 LTS"
VERSION_ID="18.04"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic
 
lsb_release -a
No LSB modules are available.
Distributor ID:   Ubuntu
Description:        Ubuntu 18.04.6 LTS
Release:              18.04
Codename:         bionic
 
hostnamectl
   Static hostname: utad
         Icon name: computer
        Machine ID: 17642ad8b86c40e7a23ee63a6d24d4ad
           Boot ID: 252b8a7a773a4e8bb00e9d6c9e3b4cef
  Operating System: Ubuntu 18.04.6 LTS
            Kernel: Linux 5.4.0-1042-raspi
      Architecture: arm



Rapsperry Pi 4: Linux verº20.07: ROS-noetic
Raspberry PI 4
cat /proc/cpuinfo
 
Model                  : Raspberry Pi 4 Model B Rev 1.
Processors: 4
BogoMIPS           : 108.00
Features              : fp asimd evtstrm crc32 cpuid
CPU implementer            : 0x41
CPU architecture: 8
CPU variant        : 0x0
CPU part             : 0xd08
CPU revision       : 3
 
Hardware            : BCM2835
Revision              : c03112
Serial                    : 1000000077cc0d0c
Model                  : Raspberry Pi 4 Model B Rev 1.2
 
cat /proc/meminfo
MemTotal:        3884324 kB
 
OS:
cat /etc/os-release
 
NAME="Ubuntu"
VERSION="20.04.2 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.2 LTS"
VERSION_ID="20.04"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
 
lsb_release -a
No LSB modules are available.
Distributor ID:   Ubuntu
Description:        Ubuntu 20.04.2 LTS
Release:              20.04
Codename:         focal
 
hostnamectl
   Static hostname: rpi4
         Icon name: computer
        Machine ID: 0f314813462c45599e46b4825c222602
           Boot ID: 45fe831cc2764fa48426dac216f3a48e
  Operating System: Ubuntu 20.04.2 LTS
            Kernel: Linux 5.4.0-1044-raspi
      Architecture: arm64

Nvidia Jetson Nano 2GB develepor kit: Ubuntu Rob3: Linux verº18.04: ROS-melodic
model name      : ARMv8 Processor rev 1 (v8l)
Processors: 4
 
BogoMIPS           : 38.40
Features              : fp asimd evtstrm aes pmull sha1 sha2 crc32
CPU implementer            : 0x41
CPU architecture: 8
CPU variant        : 0x1
CPU part             : 0xd07
CPU revision       : 1
 
cat /proc/meminfo
MemTotal:        2027380 kB
 
OS:
cat /etc/os-release
 
NAME="Ubuntu"
VERSION="18.04.5 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.5 LTS"
VERSION_ID="18.04"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic                                                                              
 
lsb_release -a
No LSB modules are available.
Distributor ID:   Ubuntu
Description:        Ubuntu 18.04.5 LTS
Release:              18.04
Codename:         bionic
 
hostnamectl
   Static hostname: nvidia
         Icon name: computer
        Machine ID: a3d9197b765643568af09eb2bd3e5ce7
           Boot ID: bca3a94ac6a84bf7a3760e89f6eb2f61
  Operating System: Ubuntu 18.04.5 LTS
            Kernel: Linux 4.9.201-tegra
      Architecture: arm64

- incluindo os links para fazer download

- Explicação de alguns dos processos

No começo deste trabalho, foi montado um carrinho simples que possui duas rodas motorizadas e uma roda na frente ao centro, tendo as placa RasperryPi 3 montada com o chapeu en-cima. A montagem que foi feita no RPI3 é feita para que tenhamos o numero de portas necessarias para fazer não só a ligação dos nossos motores para a placa mas tambem para efetuar a ligação da camera utilizada para a placa, uma coisa que se tem de ter em conta enquanto a esta montagem é o numero das portas utilizadas para transmitir a informação, sendo esses numeros que vamos indicar no codigo que irá controlar o output e input da nossa montagem.

O primeiro passo que se fez foi arranjar um cartão sd para install o sistema operativo Ubuntu versão 18.08, o motivo de ser esta versão e não a mais recente é pelo facto desta versão conter algumas funções e operações que permitam a utilização da camera que as versões mais recentes não pessuem, tendo ocorrido erros quando estas versões foram testadas.

Ao installar e fazer set-up do sistema operativo, foi instalado o ROS melodic para o projecto, tambem pode se testou instalar o ROS kinetic, no entanto, existem certas funções e operações que o kinectic não possui em comparação com o melodic para o que nos desejamos executar, dando algumas dificuldades durante o processo quando tentamos o utilizar. Para fazer a instalação, foi-se ao site do ROS.org e seguio-se os passo de instalação lá indicados. 

O catkin workspace, o espaço onde vai ser focado os nossos nodes para o trabalho, ouve alguma complicação no inicio, mas só por causa que não se percebia-se muito bem como o catkin_make funcionava. Ao perceber melhor o que catkin_make faz, e tambem perceber que tem se que executar o ficheiro setup.bat sempre que modificamos algo enquanto a direções e criações de nodes e pacotes, tornou-se mais facil de perceber como é que os pacotes e nodes se irão posicionar e ligar no catkin workspace.

Para modificar e escrever o codigo que se arranjou para o projecto foi utilizado o iditor de texto que já vinha no Ubuntu chamado Pluma, tambem se tentou escrever o codigo em c++ mas isso exigiu mais bibliotecas e funcões, que Ubuntu não pessuia, para conseguir fazer o codigo funcionar, fazer assim necessario fazer download disso tudo ocupando espaço que nos precisamos para o projeto, no entanto em python so teremos que fazer um simples apt get install para instalar o que for necessario, sendo isto não so mais rapido mas tambem mais eficiente para que o que for instalado seja utilizavel por qualquer aplicação.

Foi se fazer os exemplos que estão no site do ROS para começar a perceber a metedologia do firmware e para ajudar a perceber como as funções basicas que o ROS consegue fazer. Só depois de acabar de fazer o ultimo tutorial do nivel basico do ROS é que se começou a fazer os nodes para o projeto.
O primeiro node que se começou a tratar éra o que envolvia com o movimento das rodas, tendo em atenção que o codigo que foi arranjado na net foi modificado para que as saidas de output condizião com o comando desejado. Ao testars premeiro com comandos já dados no codigo, notou-se que havia uma diferença enquanto ao output dos pulsos dados nas saidas, tendo sido visto que éra um problema no motor em si, então foi substituido. Ao fazer mais alguns testes ao codigo, para saber como controlar a aceleração e movimento do carro, começou-se a por comandos de teclado a controlar para onde é que o carro irá se mover.

- Algumas das dificuldades encontradas
- A explicação de como funciona
- Resultados Esperados
