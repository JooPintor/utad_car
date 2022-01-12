## Instalação da camara Intel RealSense
Para proceder á instalação desta camara no Raspberry PI 3 segui [estas instruções](https://dev.intelrealsense.com/docs/using-depth-camera-with-raspberry-pi-3#section-installation-instructions) a partir do ponto 2, tendo o cuidado de fazer o __update__ do sistema operativo mas não o __upgrade__ já que me interessava manter a versão 18.04 LTS.

A sequência de ações foi a seguinte:
- Download e unzip da última versão estável do ramo mestre: https://github.com/IntelRealSense/librealsense/archive/master.zip
- _Desconectar qualquer câmera Intel RealSense conectada_
- A partir da pasta __'librealsense'__ executar os seguintes comandos/scripts:

        sudo apt-get update 
        sudo apt-get install libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev at
        ./scripts/setup_udev_rules.sh
        ./scripts/patch-realsense-ubuntu-lts.sh
        
        mkdir build && cd build
        cmake ../ -DCMAKE_BUILD_TYPE=Release -DBUILD_EXAMPLES=true
        sudo make uninstall && make clean && make -j1 && sudo make install

Este processo é bastante demorado, em particular devido á opção __-j1__, no entanto esta opção é necessária em tendo em conta os recursos nomeadamente de memória disponíveis.

