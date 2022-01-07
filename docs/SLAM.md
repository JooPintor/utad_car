## SLAM (Simultaneous Localization and Mapping)

SLAM é uma técnica utilizada por robôs e veículos autônomos para construir um mapa de um ambiente ao mesmo tempo que se localiza.

__Mapeamento__

SLAM é geralmente referenciado pelo comunidade de robótica como um processo para criar mapas geometricamente consistentes, é adaptado para as informações disponíveis no ambiente, focado-se menos na perfeição que  na conformidade operacional.

__Percepção__

SLAM pode utilizar diferentes tipos de sensores para obter informações estatisticamente independentes para minorar os erros. Independência estatística é um requisito para trabalhar com informações parciais e com métricas contendo ruídos.

__Localização__

Os resultados da percepção alimentam os algoritmos da localização. Uma abordagem utilizando visão computacional, por exemplo, pode extrair pontos de referência do ambiente que podem ser utilizados pelo algoritmo de localização para determinar a posição atual no ambiente considerando os estados anteriores do sistema.

__Modelagem__

Como parte do modelo, a cinemática do robô é incluída, consequentemente melhorando as estimativas da percepção sob condições inerentes a ruídos. O modelo dinâmico balanceia contribuições de diferentes sensores, resultando numa representação virtual do ambiente com uma núvem de probabilidade.


