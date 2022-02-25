## Instalação da camara Raspberry PI

A utilização da camara Raspberry PI no Ubuntu obriga á instalação de um conjunto de aplicativos e de drivers que devido ás especificidades do systema a que se destinam (hardwaree software) implicam a respetiva compilação pelo proprio sistema.

O primeiro passo a dar é verificar a existência de uma __swapfile__ com pelo menos 2G ([ver processo de criação de 'swapfiles'](.//Swap%20files.md)), tendo em conta os requisitos de memória necessários á compilação.

Depois é necessário garantir a instalação ds seguintes dependencias:

    $ sudo apt-get update
    $ sudo apt-get install build-essential cmake gcc g++ git unzip pkg-config
    $ sudo apt-get install libjpeg-dev libpng-dev libtiff-dev libavcodec-dev libavformat-dev libswscale-dev libgtk2.0-dev libcanberra-gtk* libxvidcore-dev libx264-dev python3-dev python3-numpy python3-pip libtbb2 libtbb-dev libdc1394-22-dev libv4l-dev v4l-utils libopenblas-dev libatlas-base-dev libblas-dev liblapack-dev gfortran libhdf5-dev libprotobuf-dev libgoogle-glog-dev libgflags-dev protobuf-compiler
  
Obter o codigo das aplicações a compilar (_opencv_ & _opencv_contrib_):

    $ cd ~
    $ wget -O opencv.zip https://github.com/opencv/opencv/archive/4.5.0.zip
    $ wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.5.0.zip

    $ unzip opencv.zip
    $ unzip opencv_contrib.zip

    $ mv opencv-4.5.0 opencv
    $ mv opencv_contrib-4.5.0 opencv_contrib
  
Criar o ficheiro __cmake__:

    $ cd opencv
    $ mkdir build
    $ cd build
    $ cmake -D CMAKE_BUILD_TYPE=RELEASE \
          -D CMAKE_INSTALL_PREFIX=/usr/local \
          -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
          -D ENABLE_NEON=ON \
          -D BUILD_TIFF=ON \
          -D WITH_FFMPEG=ON \
          -D WITH_GSTREAMER=ON \
          -D WITH_TBB=ON \
          -D BUILD_TBB=ON \
          -D BUILD_TESTS=OFF \
          -D WITH_EIGEN=OFF \
          -D WITH_V4L=ON \
          -D WITH_LIBV4L=ON \
          -D WITH_VTK=OFF \
          -D OPENCV_ENABLE_NONFREE=ON \
          -D INSTALL_C_EXAMPLES=OFF \
          -D INSTALL_PYTHON_EXAMPLES=OFF \
          -D BUILD_NEW_PYTHON_SUPPORT=ON \
          -D BUILD_opencv_python3=TRUE \
          -D OPENCV_GENERATE_PKGCONFIG=ON \
          -D BUILD_EXAMPLES=OFF ..

Compilar (pode demorar varias horas):

    $ cd ~/opencv/build
    $ make -j1
    $ sudo make install
    $ sudo ldconfig
    $ make clean
    $ sudo apt-get update


