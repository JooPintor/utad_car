## Instalação da camara Intel RealSense

Dada a dificuldade em obter a captação de imagem e respetivo tratamento ao mesmo tempo que se processa a informação dos nos ROS, foi testada a instalação da camara e respetivos módulos ROS em diferentes sistemas, com o objetivo de separar o processamento da imagem do controlo do movimento do 'utad_car'.

Os sistemas testados foram os seguintes:
- [Raspberry PI 3](#Instalação-da-camara-Intel-RealSense-no-Raspberry-PI-3)
- [Raspberry PI 4](#Instalação-da-camara-Intel-RealSense-no-Raspberry-PI-4)
- [Carta Nvidia Jetson Nano 2GB](#Instalação-da-camara-Intel-RealSense-na-carta-Nvidia-Jetson-Nano-2GB)
- [PC Portatil](#Instalação-da-camara-Intel-RealSense-no-PC-Portatil)

### Instalação da camara Intel RealSense no Raspberry PI 3
Para proceder á instalação desta camara no Raspberry PI 3 segui [estas instruções](https://dev.intelrealsense.com/docs/using-depth-camera-with-raspberry-pi-3#section-installation-instructions) a partir do ponto 2, tendo o cuidado de fazer o __update__ do sistema operativo mas não o __upgrade__ já que me interessava manter a versão 18.04 LTS.

A sequência de ações foi a seguinte:
- Download e unzip da última versão estável do ramo mestre: https://github.com/IntelRealSense/librealsense/archive/master.zip
- _Desconectar qualquer câmara Intel RealSense conectada_
- A partir da pasta __'librealsense-master'__ executar os seguintes comandos/scripts:

        sudo apt-get update 
        sudo apt-get install libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev 
        ./scripts/setup_udev_rules.sh
        
        mkdir build && cd build
        cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_EXAMPLES=true -DBUILD_PYTHON_BINDINGS:bool=true -DFORCE_RSUSB_BACKEND=ON -DPYTHON_EXECUTABLE=/usr/bin/pyt
        sudo make uninstall && make clean && make -j1 && sudo make install
        
        sudo apt-get install qt5-default

Este processo é bastante demorado, em particular devido á opção __-j1__, no entanto esta opção é necessária em tendo em conta os recursos nomeadamente de memória disponíveis.

Nota: A capacidade de RAM pode não ser suficiente para compilar o SDK, portanto, se o processo de compilação abortar com um código de erro, uma solução poderá ser criar uma [‘sawp file’](./Swap%20files.md) e recompilar o SDK

Depois de instalados o software da camara deverá ser possível testar a instalação recorrendo á aplicação __'realsense-viewer'__ executando o comando e obtendo o resultado seguintes:

        realsense-viewer

![RealSense-Viewer](../imgs/RealSense-Viewer.jpg)

- Instalação dos módulos ROS para utilização da camara

        cd ~/catkin_ws
        sudo apt-get install ros-$ROS_DISTRO-realsense2-camera
        sudo apt-get install ros-$ROS_DISTRO-realsense2-description

- Depois de instalados os módulos ROS pode-se executar os seguintes comandos e obter o resultado apresentado a seguir:

        export ROS_MASTER_URI=http://localhost:11311
        source ~/catkin_ws/devel/setup.bash
        cd ~/catkin_ws
        roslaunch realsense2_camera rs_d435_camera_with_model.launch

![rs_d435_camera_with_model](../imgs/rs_d435_camera_with_model.jpg)

### Instalação da camara Intel RealSense no Raspberry PI 4
Para proceder á instalação desta camara no Raspberry PI 4 segui [estas instruções](https://answers.ros.org/question/363889/intel-realsens-on-ubuntu-2004-ros-noetic-installation-desription/). De notar que embora esta página já esteja ultrapassada para arquiteturas X86/AMD64, pareceu-me a mais apropriada para a arquitetura ARM64.


A sequência de ações foi a seguinte:
- Download e unzip da última versão estável do ramo mestre: https://github.com/IntelRealSense/librealsense/archive/master.zip
- _Desconectar qualquer câmara Intel RealSense conectada_
- A partir da pasta __'librealsense-master'__ executar os seguintes comandos/scripts:

        sudo apt-get update
        sudo apt-get install guvcview git libssl-dev libusb-1.0-0-dev pkg-config libgtk-3-dev
        sudo apt-get install libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev 
        sudo mkdir -p /opt/realsense
        
        cmake -DFORCE_RSUSB_BACKEND=true -DBUILD_PYTHON_BINDINGS=false -DCMAKE_BUILD_TYPE=release -DBUILD_EXAMPLES=true -DBUILD_GRAPHICAL_EXAMPLES=true -DCMAKE_INSTALL_PREFIX=$REALSENSE_INSTALL_PREFIX
        sudo make uninstall && make clean && make -j1 && sudo make install
        
        sudo bash -c "echo /opt/realsense/lib > /etc/ld.so.conf.d/realsense.conf"
        
        sudo cp config/99-realsense-libusb.rules /etc/udev/rules.d/99-realsense-libusb.rules 
        sudo udevadm control --reload-rules && udevadm trigger
        
        echo "export realsense2_DIR=/opt/realsense/lib/cmake/realsense2" >> ~/.bashrc

Este processo é bastante demorado, em particular devido á opção __-j1__, no entanto esta opção é necessária em tendo em conta os recursos nomeadamente de memória disponíveis.

Nota: A capacidade de RAM pode não ser suficiente para compilar o SDK, portanto, se o processo de compilação abortar com um código de erro, uma solução poderá ser criar uma [‘sawp file’](./Swap%20files.md) e recompilar o SDK

Depois de instalados o software da camara deverá ser possível testar a instalação recorrendo á aplicação __'realsense-viewer'__ executando o comando seguinte:

        /opt/realsense/bin/realsense-viewer

![realsense-viewer-rpi4](../imgs/realsense-viewer-rpi4.jpg)


- Instalação dos módulos ROS para utilização da camara

        cd ~/catkin_ws
        git clone https://github.com/IntelRealSense/realsense-ros.git ~/catkin_ws/src/realsense-ros
        catkin_make

- Depois de instalados os módulos ROS pode-se executar os seguintes comandos e obter o resultado apresentado a seguir:

        export ROS_MASTER_URI=http://localhost:11311
        source ~/catkin_ws/devel/setup.bash
        cd ~/catkin_ws
        roslaunch realsense2_camera rs_d435_camera_with_model.launch

![rs_d435_camera_with_model-rpi4](../imgs/rs_d435_camera_with_model-rpi4.jpg)

### Instalação da camara Intel RealSense na carta Nvidia Jetson Nano 2GB

Com o objetivo de tirar o máximo partido das capacidades desta carta para processamento de vídeo, o SO adotado foi o retirado da imagem  __'jetson-nano-2gb-jp451-sd-card-image.zip'__.

Este SO apresenta a seguinte mensagem quando nos conectamos por SSH:

        Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 4.9.201-tegra aarch64)

         * Documentation:  https://help.ubuntu.com
         * Management:     https://landscape.canonical.com
         * Support:        https://ubuntu.com/advantage
        This system has been minimized by removing packages and content that are
        not required on a system that users do not log into.

        To restore this content, you can run the 'unminimize' command.

Como se pode ver trata-se do Sistema operativo ubuntu 18.04.05 LTS com um núcleo GNU/Linux 4.9.201-tegra e uma arquitetura ARM64.

#### Instalação do vncserver na carta Nvidia Jetson Nano

Na sequência da instalação do servidor e do acesso por SSH, procedi ao comando __'unminimize'__ para permitir o acesso ao sistema com interface gráfico.
A instalação do acesso á distância quer por __xrdp__ quer por __VNC__ revelou-se de difícil configuração, pelo que acabei por seguir as instruções [desta página](https://jinyaozhu.github.io/linux/2019/05/16/vnc.html), sem no entanto instalar outro servidor vnc ou outro desktop.

Os comandos de configuração do serviço VNC foram os seguintes:

        vncserver
        vncserver -kill :1
        
        sudo vi ~/.vnc/xstartup
        
        #Alterar o conteúdo do ficheiro 'xstartup' para:
                #!/bin/bash
                unset SESSION_MANAGER
                unset DBUS_SESSION_BUS_ADDRESS
                xrdb $HOME/.Xresources
                startlxde &
        
        # Arrancar o servidor 
        vncserver :1 -geometry 1360x768 -depth 24
        
        # Testar a ligação
        
        # Em caso de sucesso criar um serviço que arranque o servidor ao ligar
        
        sudo vim /etc/systemd/system/vncserver@.service
        
        #Alterar o conteúdo do ficheiro para:        
                [Unit]
                Description=Start VNC server at startup
                After=syslog.target network.target

                [Service]
                Type=forking
                User=!!!user_name!!!
                Group=!!!user_name!!!
                WorkingDirectory=/home/!!!user_name!!!

                PIDFile=/home/!!!user_name!!!/.vnc/%H:%i.pid
                ExecStartPre=-/usr/bin/vncserver -kill :%i > /dev/null 2>&1
                ExecStart=/usr/bin/vncserver -depth 24 -geometry 1360x768 :%i
                ExecStop=/usr/bin/vncserver -kill :%i

                [Install]
                WantedBy=multi-user.target
        
        sudo systemctl daemon-reload
        sudo systemctl enable vncserver@1.service
        vncserver -kill :1
        sudo systemctl start vncserver@1
        sudo systemctl status vncserver@1
        
Não esquecer de substituir !!!user_name!!! pelo nome do utilizador do SO.

Após o último comando deverá surgir uma informação semelhante á seguinte:

![status do vncserver](../imgs/status%20do%20vncserver.jpg)


#### Instalação do ROS na carta Nvidia Jetson Nano 

Neta carta, tendo em conta o SO em presença selecionou-se a instalação do ROS Melodic seguindo as instruções [desta página](http://wiki.ros.org/Installation/Ubuntu) e utilizando os seguintes comandos:

        sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
        sudo apt install curl
        curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
        sudo apt update
        sudo apt install ros-melodic-desktop-full
        echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
        source ~/.bashrc
        sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
        sudo apt install python-rosdep
        sudo rosdep init
        rosdep update
        mkdir -p ~/catkin_ws/src
        cd ~/catkin_ws/
        catkin_make
        source devel/setup.bash

#### Instalação do SDK da camara 

Para proceder á instalação do SDK desta camara na carta segui [estas instruções](https://github.com/IntelRealSense/librealsense/blob/master/doc/installation_jetson.md), utilizando os comandos seguintes:

        sudo apt-get update
        sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE
        sudo add-apt-repository "deb https://librealsense.intel.com/Debian/apt-repo $(lsb_release -cs) main" -u 
        
        sudo apt-get install librealsense2-utils
        sudo apt-get install librealsense2-dev
        
        realsense-viewer

Na sequência do comando _'realsense-viewer'_ obtive o erro seguinte:

        GLFW Driver Error: GLX: GLX version 1.3 is required
        Could not initialize offscreen context!

Admitindo que o erro poderia resultar de estar ligado por VNC liguei-me com um teclado e um monitor pela porta HDMI e voltei a tentar o mesmo comando, obtendo a seguinte mensagem:

        libGL error: MESA-LOADER: failed to open swrast (search paths /usr/lib/aarch64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri)
        libGL error: failed to load driver: swrast
        GLFW Driver Error: Requested OpenGL version 1.0, got version 0.0
        Could not initialize offscreen context!

Não tendo encontrado uma solução para este problema e tendo em conta o tempo já utilizado na instalação do VNC, acabei por abandonar esta opção de processamento da imagem da camara Intel RealSense.

### Instalação da camara Intel RealSense no PC Portátil

A instalação do SDK da camara Realsense revelou-se bastante simples, bastando proceder ao Download do mesmo a partir [desta página](https://www.intelrealsense.com/sdk-2/).

Para o efeito selecionei os seguintes módulos:

   - [Depth.Quality.Tool.exe]
   - [Intel.RealSense.SDK-WIN10-2.50.0.3785.exe]
   - [Intel.RealSense.Viewer.exe]

Tratando-se de módulos .exe após o download estão prontos a utilizar.

#### Instalação dos módulos ROS para utilização da camara
Tentei várias alternativas para arranjar os pacotes da camara para o sistema Windows, incluindo o _“Windows Package Manager”_ desenvolvido pela Microsoft, no entanto verifiquei que esta ferramenta está limitada a uma lista de softwares que não inclui os drives da camara _“RealSense”_.

O _“Chocolatey”_ permitiu o download dos pacotes desejados, no entanto mesmo assim não consegui instalá-los de forma a serem reconhecidos pelo ROS.
Tendo em conta as dificuldades encontradas, abandonei a hipótese de utilização do Windows como possível servidor ROS com processamento das informações dadas pela camara RealSense.

