## O que é ROS?
O __Robot Operating System__ (ROS, sistema operativo de robôs) é uma coleção de frameworks de software para desenvolvimento e programação de robôs, que fornece as funcionalidades dum sistema operativo num cluster de computadores heterogêneo.

O ROS fornece serviços normalmente fornecidos pelos sistemas operativos, tais como abstração de hardware, controle de dispositivos de baixo nível, a implementação de funcionalidades comumente usadas, tais como passagem de mensagens entre processos e gestão de pacotes.

O conjunto de processos do ROS em execução são representados numa arquitetura gráfica onde o processamento é realizado nos nós que podem receber e enviar mensagens, tais como valores de sensores, controle, estado, planeamento, atuadores e outras.

Apesar da importância da reatividade e baixa latência no controle de robôs, o ROS em si, não é um sistema operativo de tempo real, embora seja possível integrar o ROS com código em tempo real.

O Software do ecossistema ROS pode ser dividido em três grupos:
- Ferramentas independentes da linguagem e plataforma usadas para a construção e distribuição de software baseado em ROS;
- Implementações de bibliotecas clientes de ROS como roscpp, rospy e roslisp;
- Pacotes com código relacionado com aplicações que usam uma ou mais bibliotecas cliente de ROS.

Tanto as ferramentas independentes da língua como as principais bibliotecas clientes (C++, Python e Lisp) são lançadas sob os termos da licença BSD, e como tal são softwares de fonte aberta e livre para uso comercial e de investigação.

A maioria dos outros pacotes estão licenciados sob uma variedade de licenças de código aberto. Estes outros pacotes implementam funcionalidades e aplicações, tais como drivers de hardware, modelos de robôs, tipos de dados, planeamento, perceção, mapeamento e localização simultâneos, ferramentas de simulação e outros algoritmos comumente usados.

 Para saber mais pode-se ir ao site do [ROS](http://wiki.ros.org/)
