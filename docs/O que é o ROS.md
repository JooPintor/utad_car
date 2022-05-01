## O que é o ROS
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

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Como o nome completo do 'Robot Operating System' sugere, o ROS é um sistema operativo para robôs.
Da mesma forma que os sistemas operativos para PCs, servidores ou dispositivos autónomos, o ROS é um sistema operativo completo para os serviços da robótica.
O ROS é de fato um meta-sistema operativo, algo entre um sistema operativo e um middleware. É um conjunto de bibliotecas de software livre de código aberto que ajudam seus utilizadores a desenvolver aplicações de robótica.

Ele fornece uma variedade de recursos padrão para um sistema operativo, tais como:
- Abstração de hardware
- Gestão de contenção
- Gestão de processos

O ROS também fornece funcionalidade de alto nível:
- Chamadas assíncronas
- Chamadas síncronas
- Banco de dados centralizado
- Sistema de configuração do robô

### Vantagens e história do ROS

Antes da existência dos sistemas operativos de robôs, todo o projetista de robôs e investigador de robótica gastava uma quantidade considerável de tempo projetando o software embarcado dentro de cada robô, bem como o próprio hardware. Isso exigia habilidades em engenharia mecânica, eletrónica e programação embarcada. Normalmente, os programas projetados dessa maneira eram parecidos com a programação embarcada, mais semelhante à eletrónica, do que à robótica no sentido mais estrito, como podemos encontrar hoje em dia na robótica. Houve uma reutilização considerável de programas, pois eles estavam fortemente ligados ao hardware subjacente.

A ideia principal de um sistema operativo robótico é evitar reinventar a roda continuamente e oferecer funcionalidades padronizadas realizando a abstração do hardware, assim como um sistema operativo convencional para PCs, daí o nome análogo.

ROS é um facilitador de projetos de robótica. Investigadores ou engenheiros em divisões de I\&D que usam ROS já não gastam tempo a criar um novo ecossistema para cada novo projeto de robótica, o que também representa um ganho financeiro.

O ROS tem um impacto positivo em I&D, reduzindo custos e o “time to market”. Para estruturas ou departamentos cujo objetivo é lançar um novo protótipo rapidamente, ou que precisam reduzir uma lacuna tecnológica, torna-se bastante atraente.

Outro benefício dos sistemas operativos de robôs, como o ROS, é a combinação de conhecimentos de diferentes disciplinas. De fato, projetar e programar um robô significa:
- Gestão do hardware e escrita dos drivers
- Gestão da memória e de processos
- Gestão de simultaneidade, paralelismo e fusão de dados
- Fornecer algoritmos de raciocínio abstrato, utilizando inteligência artificial

A robótica, portanto, requer conjuntos de habilidades muito diferentes, geralmente para lá do alcance de um único indivíduo.
O ROS reduz o nível técnico necessário para trabalhar em projetos de robótica e tornar mais fácil a iniciação na robótica e o projeto de sistemas complexos.
