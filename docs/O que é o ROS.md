## O que é o ROS

Como o nome completo sugere, o __Robot Operating System__ é um sistema operativo para robôs.
Da mesma forma que os sistemas operativos para PCs, servidores ou dispositivos autónomos, o ROS é um sistema operativo completo para os serviços da robótica.
O ROS é de fato um meta-sistema operativo, algo entre um sistema operativo e um middleware. É um conjunto de bibliotecas de software livre de código aberto que ajudam os utilizadores a desenvolver aplicações de robótica.

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

Antes da existência dos sistemas operativos de robôs, os projetistas de robôs e investigador de robótica gastava uma quantidade considerável de tempo a projetar o software embarcado dentro de cada robô, bem como o próprio hardware. Isso exigia competências em engenharia mecânica, eletrónica e programação embarcada. Normalmente, os programas projetados dessa maneira eram parecidos com a programação embarcada, mais semelhante à eletrónica, do que à robótica no sentido mais estrito, como podemos encontrar hoje em dia na robótica.

A ideia principal de um sistema operativo robótico é evitar reinventar a roda continuamente e oferecer funcionalidades padronizadas realizando a abstração do hardware, tal como um sistema operativo convencional para PCs, daí o nome análogo.

ROS é um facilitador de projetos de robótica. Investigadores ou engenheiros em divisões de I&D que usam ROS já não gastam tempo a criar um novo ecossistema para cada novo projeto de robótica, o que também representa um ganho financeiro.

Outro benefício dos sistemas operativos de robôs, como o ROS, é a combinação de conhecimentos de diferentes disciplinas. De fato, projetar e programar um robô significa:
- Gestão do hardware e escrita dos drivers
- Gestão da memória e de processos
- Gestão de simultaneidade, paralelismo e fusão de dados
- Fornecer algoritmos de raciocínio abstrato, utilizando inteligência artificial

A robótica, portanto, requer conjuntos de competẽncias muito diferentes, geralmente para lá do alcance de um único indivíduo.
O ROS reduz o nível técnico necessário para trabalhar em projetos de robótica e tornar mais fácil a iniciação na robótica e o projeto de sistemas complexos.

Existem muitos frameworks de robôs, produzidos por um motivo específico, para fins de prototipagem.

O ROS foi planeado para ser de uso mais geral, embora os seus designers não acreditem que seja o sistema operativo definitivo capaz de fazer tudo.

Antes de 2007, o ano do lançamento do ROS, os engenheiros de robótica não tinham uma arquitetura de software embarcada padrão. É por isso que o ROS é um grande salto em frente.

O ROS é desenvolvido e mantido por uma empresa californiana, Willow Garage, formada em 2006 por Scott Hassan, um dos primeiros funcionários do Google que esteve envolvido no desenvolvimento da tecnologia de mecanismos de busca e que também esteve por trás do Yahoo! Grupos (eGroups, na verdade, que se tornaram Yahoo! Groups).
 
Willow Garage é uma empresa privada que mantém ligações estreitas com a Universidade de Stanford, que não fica longe de Willow Garage (em Palo Alto, Califórnia).
Willow Garage pode ser descrita como um laboratório de pesquisa e incubadora de tecnologia para robótica pessoal, focado mais na pesquisa do que no nos lucros (no início, pelo menos).

A Willow Garage desenvolve software com ROS e hardware com seus robôs PR2 e TurtleBot. Tudo o que é produzido é de código aberto (licenças BSD). A ideia deles é que, se quisermos que os robôs cheguem às nossas casas, a pesquisa precisa ser acelerada, fornecendo bases sólidas de hardware e software de código aberto.

### Organização geral e programação do ROS

A filosofia ROS pode ser resumida nos cinco seguintes princípios principais:
- Peer to Peer
- Multi-idioma
- Baseado em ferramentas (microkernel)
- Leve
- Gratuito e de código aberto

Cobrindo cada ponto:
#### Peer to Peer
Um robô suficientemente complexo compreende vários computadores de bordo ou placas conectadas via Ethernet, além de, às vezes, computadores externos para tarefas de computação intensivas. Uma arquitetura peer-to-peer acoplada a um sistema de buffer e um sistema de pesquisa (um serviço de nomes chamado 'master' no ROS), permite que cada componente converse diretamente com qualquer outro, de forma síncrona ou assíncrona, conforme necessário.
#### Multi-idioma
o ROS é neutro em termos de idioma e pode ser programado em vários idiomas. A especificação ROS funciona na camada de mensagens. As conexões peer-to-peer são negociadas em XML-RPC, que existe num grande número de linguagens. Para suportar uma nova linguagem, as classes C++ são reempacotadas (o que foi feito para o cliente Octave, por exemplo) ou as classes são escritas permitindo a geração de mensagens. Essas mensagens são descritas em IDL (Interface Definition Language).
#### Baseado em ferramentas
Em vez de um ambiente de tempo de execução monolítico, o ROS adotou um design de microkernel, que usa um grande número de pequenas ferramentas para construir e executar os vários componentes do ROS. À medida que se abordam os tutoriais do ROS, aprende-se a usar vários comandos utilizados para manipular nós e mensagens. Cada comando é de fato um executável. A vantagem deste sistema é que um problema com um executável não afeta os demais, o que torna o sistema mais robusto e flexível do que um sistema baseado num ambiente de tempo de execução centralizado
#### Leve
Para combater o desenvolvimento de algoritmos que estão  em menor ou maior grau ligados ao sistema operativo robótico e, portanto, são difíceis de reutilizar posteriormente, os desenvolvedores de ROS pretendem que drivers e outros algoritmos sejam contidos em executáveis autónomos. Isso garante a máxima reutilização e, acima de tudo, mantém o seu tamanho reduzido. Este método torna o ROS fácil de usar, encontrando-se a maior complexidade nas bibliotecas. Esse arranjo também facilita o teste de unidade. Por fim, o ROS usa código (drivers e algoritmos) de outros projetos de código aberto, tais como:
- Simuladores de projeto
- Bibliotecas de processamento de imagem e visão artificial do OpenCV
- Algoritmos de planeamento do OpenRave
#### Gratuito e de código aberto
Já explicamos os motivos dessa escolha. Observe, no entanto, que a arquitetura escolhida é consistente com essa escolha. O ROS passa dados entre módulos usando comunicações entre processos e, como resultado, os módulos não precisam ser vinculados num único processo, possibilitando o uso de diferentes licenças.

O ecossistema ROS possui funcionalidades de partilha integradas. O ROS permite importar e exportar bibliotecas de software (pacotes ROS) que podem ser carregadas e enviadas para www.ros.org. Esses recursos criaram um ambiente aberto para colaboração e partilha de conhecimento na comunidade de robótica.

### Programação no ROS
O ROS é independente de idioma. Neste momento, três bibliotecas principais foram definidas para ROS, tornando possível programar ROS em Python, Lisp ou C++. Além dessas três bibliotecas, duas bibliotecas experimentais são oferecidas, possibilitando a programação do ROS em Java ou Lua.

### O sistema de arquivos ROS

Os recursos ROS são organizados numa estrutura hierárquica em disco. Destaco dois conceitos importantes:
- __pacote (Package)__

A unidade fundamental dentro da organização do software ROS. Um pacote é um diretório contendo nós (nós são explicados abaixo), bibliotecas externas, dados, arquivos de configuração e um arquivo de configuração xml chamado manifest.xml.
- __pilha (Stacks)__

Uma coleção de pacotes. Ela oferece um conjunto de funcionalidades como navegação, posicionamento, etc. Uma pilha é um diretório contendo diretórios de pacotes mais um arquivo de configuração chamado stack.xml.

Além dessas duas noções muito importantes, também vale a pena notar a ideia de ‘uma distribuição’, que é, como no Linux, uma coleção de pilhas versionadas.

### Noções básicas de ROS
O princípio básico de um sistema operativo de robô é executar um grande número de executáveis em paralelo que devem ser capazes de trocar dados de forma síncrona ou assíncrona. Por exemplo, um sistema operativo de robótica precisa de consultar os sensores do robô a uma frequência definida (sensor de distância de ultra-som ou infravermelho, sensor de pressão, sensor de temperatura, giroscópio, acelerômetro, câmeras, microfone, etc.), recuperar esses dados, processá-los (integrar a informação recebida na existente 'data merge'), passá-lo para algoritmos de processamento (processamento de fala, visão artificial, SLAM – localização e mapeamento simultâneos, etc.) e por último controlar os motores. Todo este processo é realizado de forma contínua e paralela. Além disso, o sistema operativo de robótica precisa gerir a contenção para garantir o acesso eficiente aos recursos do robô.

Os conceitos reunidos no ROS sob o nome de “ROS Computation Graph”, permitindo que esses objetivos sejam alcançados, são descritos a seguir. Estes são conceitos usados pelo sistema em execução, enquanto o 'ROS File System' descrito na seção anterior é um conceito estático.

#### Nós (node)
O ROS aborda toda a sua problemática usando algumas noções básicas simples. A primeira delas é a noção de nó.
No ROS, um nó é uma instância de um executável. Um nó pode equivaler a um sensor, motor, algoritmo de processamento ou monitoramento e assim por diante. Cada nó que começa a ser executado é declarado no Mestre. Isso leva à arquitetura de microkernel, em que cada recurso é um nó independente.
Graças ao sistema de nós, as funções básicas podem ser padronizadas e os blocos de construção tecnológicos podem ser desenvolvidos rapidamente e facilmente reutilizados, modificados ou aprimorados.

#### Mestre (Master)
O Master é um serviço de declaração e registro de nós, que possibilita que os nós se encontrem e troquem dados. O Master é implementado via XMLRPC.
O Master inclui um componente muito utilizado chamado 'Parameter Server', também implementado na forma de XMLRPC, e que é, como o nome indica, uma espécie de banco de dados centralizado no qual os nós podem armazenar dados e, ao fazê-lo, compartilhar informações e parâmetros visiveis por todo o sistema.

#### Tópicos (topic)
Os dados são trocados de forma assíncrona por meio de um tópico e de forma síncrona por meio de um serviço.

Um tópico é um sistema de transporte de dados baseado num sistema de assinatura/publicação. Um ou mais nós podem publicar dados num tópico e um ou mais nós podem ler dados nesse tópico. Um tópico é, de certa forma, um barramento de mensagens assíncrono, um pouco como um feed RSS. Essa noção de um barramento assíncrono, muitos para muitos, é essencial numa situação de sistema distribuído.
Um tópico é digitado, o que significa que o tipo de dado publicado (a mensagem) é sempre estruturado da mesma forma. Os nós enviam e recebem mensagens sobre tópicos.

#### Mensagens (messages)
Uma mensagem é uma estrutura de dados composta. Uma mensagem compreende uma combinação de tipos primitivos (strings de caracteres, booleanos, inteiros, ponto flutuante, etc.) e mensagens (uma mensagem é uma estrutura recursiva). Por exemplo, um nó representando um servo-motor do robô certamente publicará seu estado num tópico (dependendo de como for programado) com uma mensagem contendo, por exemplo, um inteiro representando a posição do motor, um número de vírgula flutuante para sua temperatura, outro número de vírgula flutuante para sua velocidade, e assim por diante.
A descrição da mensagem é armazenada em package_name/msg/myMessageType.msg. Este arquivo descreve a estrutura da mensagem.

#### Serviços (services)
Um tópico é um método de comunicação assíncrono usado para comunicação muitos para muitos. Um serviço atende a um tipo diferente de necessidade, a de comunicação síncrona entre dois nós. A ideia é semelhante à de uma chamada de um procedimento remoto.

A descrição do serviço é armazenada em package_name/srv/myServiceType.srv. Este arquivo descreve as estruturas de dados para solicitações e respostas.

![ROS-Topics.jpg](../imgs/ROS-Topics.jpg)

#### Bolsas (Bags)
Bags são formatos para armazenar e reproduzir dados de mensagens. Esse mecanismo possibilita, por exemplo, coletar dados medidos por sensores e, posteriormente, reproduzi-los quantas vezes desejarmos para simular dados reais. Também é um sistema muito útil para depurar o sistema após um evento.

A ferramenta rxbag pode ser usada para exibir dados gravados em arquivos bag em forma gráfica.

### URDF
O ROS fornece ainda outros conceitos que poderemos encontrar na Internet, é no entanto relevante, mencionar uma outra interessante contribuição para a robótica a partir do ROS que é o formato URDF (Unified Robot Description Format).

Trata-se de um formato XML usado para descrever um robô inteiro na forma de um arquivo padronizado.

Robôs descritos desta forma podem ser estáticos ou dinâmicos e as propriedades físicas e de colisão podem ser incluídas

Além do padrão, o ROS oferece diversas ferramentas utilizadas para gerar, analisar ou verificar este formato

O URDF é usado pelo simulador Gazebo, por exemplo, para representar o robô.

### ROS2
O ROS foi desenvolvido numa primeira fase para o mundo académico (pesquisa, ensino superior). Este ecossistema não está, por isso, alinhado com os padrões de produção industriais.

Uma nova versão, ROS2, foi lançada em 2017. Esta versão preenche as lacunas do ROS em termos de segurança e fiabilidade.

O ROS2 traz qualidade de serviço, suporte para sistemas embarcados e cenários em tempo real.

 Para saber mais pode-se ir ao site do [ROS](http://wiki.ros.org/)
