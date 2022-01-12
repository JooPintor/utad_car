## Utilização da camara Intel RealSense
A utilização de camaras com capacidade de captação de imagem e informação de profundidade, como é o caso da [Intel RealSense](./Camara%20Intel%20RealSense.md),apresenta-se como uma alternativa a considerar nos sistemas de navegação autónoma.

Esta camaras para além da deteção da distância aos obstáculos permitem a identificação de marcas estáticas no seu ambiente, localizando-se a partir a partir das mesmas ou localizar elementos móveis, permitindo o estabelecimento de trajetórias em função da sua localização relativa.

Para estudar o comportamento desta camara começou-se pela [sua instalação](./Instalação%20da%20camara%20Intel%20RealSense.md).

No entanto, a captação e o processamento de imagens em simultâneo com as restantes funções de controlo revelou-se um desafio difícil de superar utilizando apenas o Raspberry PI 3, pelo que foi explorada a possibilidade de separar a captação da imagem e o controlo de baixo nível do controlo de alto nível, instalando o ROS em dois locais, com processamento independente e comunicação pela rede LAN.

Foram assim estudadas as seguintes hipóteses de locais de processamento, admitindo que a captação de imagens se faria sempre ao nível do 'Raspberry PI 3':
- [Raspberry PI3](#Processamento-da-Imagem-no-Raspberry-PI-3)
- [Raspberry PI 4](#Processamento-da-Imagem-no-Raspberry-PI-4)
- [PC Portatil]()
- [Carta Nvidia Jetson Nano]()

### Processamento da Imagem no Raspberry PI 3
