## Instalação do ROS
O processo de instalação do ROS depende do sistema operativo e do hardware em que o mesmo é instalado.

Tendo a sido disponibilizado pela universidade um SBC [Raspberry PI 3](./docs/Raspberry%20PI%203.md), foi sobre esse hardware que incidiram maioritáriamente os estudos das diferentes alternativas, no entanto tambem foram testados o [Raspeberry PI 4](./docs/Raspberry%20PI%204.md), o [Nvidia Jetson Nano](./docs/Nvidia%20Jetson%20Nano%202GB%20develepor%20kit.md) e a instalação do ROS num [PC Portátil]() com Windows.

Tendo o Raspberry PI 3 de uma arquitetura __armhf__ e memória limitada, verificou-se que a melhor combinação de sistema operativo e versão de ROS para este SBC é o sistema operativo __ubuntu 18.04 bionic__ e o __ROS Melodic__. 

Para o Raspberry PI 4 a preferencia recaiu sobre o sistema operativo __ubuntu 20.04 focal__ e o __ROS Noetic__

A instalação do ROS foi feita a partir das instruções disponíveis no site da Organisação ROS, o [ROS-Wiki](http://wiki.ros.org/ROS/Installation).

Note-se que nem todas as arquiteturas de processadores e sistemas opertivos têm imagens disponoiveis para instalação, pelo que em alguns casos foi necessário compilar o código fonte no sistema em que se pretendia fazer a instalação.

A compilação do código fonte do ROS,para além de demorar algum tempo exige a disponibilidade de recursos, em particular a memória, pelo que se deve garantir uma __"swap file"__ com dimensão suficiente para que a compilação tenha sucesso.

A verificação ou alteração da "swap file" pode ser feita seguindo [estas](./docs/Swap%20files.md) instruçẽs.

