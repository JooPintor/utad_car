## Instalação do ROS
O processo de instalação do ROS depende do sistema operativo e do hardware em que o mesmo é instalado.

Tendo a universidade disponibilizado um SBC [Raspberry PI 3](./Raspberry%20PI%203.md), foi sobre esse hardware que incidiram maioritariamente os estudos das diferentes alternativas, no entanto também foram testados o [Raspberry PI 4](./Raspberry%20PI%204.md), o [Nvidia Jetson Nano](./Nvidia%20Jetson%20Nano%202GB%20develepor%20kit.md) e a instalação do ROS num [PC Portátil](./Portátil%20ASUS%20Laptop%20X512DA.313.md) com Windows.

Tendo o Raspberry PI 3 de uma arquitetura __armhf__ e memória limitada, verificou-se que a melhor combinação de sistema operativo e versão de ROS para este SBC é o sistema operativo __ubuntu 18.04 bionic__ e o __ROS Melodic__. 

Para o Raspberry PI 4 a preferência recaiu sobre o sistema operativo __ubuntu 20.04 focal__ e o __ROS Noetic__

Para o [PC Portátil](./Portátil%20ASUS%20Laptop%20X512DA.313.md), com o SO Windows 10, optou-se pela instalação __ROS Melodic__ por se tratar da distribuição mais estável para o este sistema operativo. 

A instalação do ROS foi feita a partir das instruções disponíveis no site da Organização ROS, o ROS-Wiki. Para os SBCs com SO Linux seguiu-se  [esta](http://wiki.ros.org/Installation) página e para PC Portátil com SO Windows seguiu-se [esta](http://wiki.ros.org/Installation/Windows).

Note-se que nem todas as arquiteturas de processadores e sistemas operativos têm imagens disponíveis para instalação, pelo que em alguns casos foi necessário compilar o código fonte no sistema em que se pretendia fazer a instalação.

A compilação do código fonte do ROS, para além de demorar algum tempo exige a disponibilidade de recursos, em particular a memória, pelo que se deve garantir uma __"swap file"__ com dimensão suficiente para que a compilação tenha sucesso.

A verificação ou alteração da "swap file" pode ser feita seguindo [estas](./Swap%20files.md) instruções.

Verifiquei no processo de instalação do ROS no Windows que para ter sucesso é necessário desativar completamente software antivírus e de firewall, já que os mesmos interferem com o processo de instalação. Como tanto os pacotes do ROS como do Chocolatey provêm de fontes não identificadas, o antivírus trata-os como vírus, impedindo-os de ser executados. No caso de tal ocorrer, torna-se necessário desinstalar tudo o que já tenha sido instalado, desativar as proteções do computador e recomeçar a instalação.

Uma dificuldade na instalação do ROS no sistema Windows, resulta deste sistema operativo não possuir repositórios e ferramentas como o _"apt get"_ do ubuntu, que nos permita transferir e controlar as transferências dos pacotes necessários tal como se pode fazer nos sistemas Linux a partir da linha de comandos. 

