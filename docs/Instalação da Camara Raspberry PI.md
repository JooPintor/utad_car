## Instalação da camara Raspberry PI

A utilização da camara Raspberry PI no Ubuntu obriga á instalação de um conjunto de aplicativos e de drivers que devido ás especificidades do systema a que se destinam (hardwaree software) implicam a respetiva compilação pelo proprio sistema.

O primeiro passo a dar é verificar a existência de uma __swapfile__ com pelo menos 2G ([ver processo de criação de 'swapfiles'](.//Swap%20files.md)), tendo em conta os requisitos de memória necessários á compilação.

Depois é necessário garantir a instalação ds seguintes dependencias:

  $ sudo apt-get update
  $ sudo apt-get install build-essential cmake gcc g++ git unzip pkg-config
  $ sudo apt-get install libjpeg-dev libpng-dev libtiff-dev libavcodec-dev libavformat-dev libswscale-dev libgtk2.0-dev libcanberra-gtk* libxvidcore-dev libx264-dev python3-dev python3-numpy python3-pip libtbb2 libtbb-dev libdc1394-22-dev libv4l-dev v4l-utils libopenblas-dev libatlas-base-dev libblas-dev liblapack-dev gfortran libhdf5-dev libprotobuf-dev libgoogle-glog-dev libgflags-dev protobuf-compiler
  
  
  
