## Utilização da camara Intel RealSense
A utilização de camaras com capacidade de captação de imagem e informação de profundidade, como é o caso da [Intel RealSense](./Camara%20Intel%20RealSense.md),apresenta-se como uma alternativa a considerar nos sistemas de navegação autonuma.

São versáteis, já que para além da deteção da distância aos obstaculos permite a identificação de marcas estáticas no seu âmbiente, localizando-se a partir a partir das mesmas ou localizar elementos móveis, permitindo o establecimento de trajetórias em função da sua localização relativa.

No entanto, a captação e o processamento de imagens em simultaneo com as restantes funções de controlo reveluo-se um desafio dificil de superar utilizando apenas o Raspberry PI 3, pelo que tentei uma abordagem de instalação do ROS em dois locais, separando a captação de imagem do seu processamento.

Foram estudadas as seguintes hipotesess de locais de processamento:
- [Carta Nvidia Jetson Nano]()
- [Raspberry PI 4]()
- [PC Portatil]()
