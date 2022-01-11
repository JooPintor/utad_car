## Utilização da camara Intel RealSense
A utilização de camaras com capacidade de captação de imagem e informação de profundidade, como é o caso da [Intel RealSense](./Camara%20Intel%20RealSense.md),apresenta-se como uma alternativa a considerar nos sistemas de navegação autonuma.

São versáteis, já que para além da deteção da distância aos obstaculos permite a identificação de marcas estáticas no seu âmbiente, localizando-se a partir a partir das mesmas ou localizar elementos móveis, permitindo o establecimento de trajetórias em função da sua localização relativa.

Para estudar o comportamento desta camara comessou-se pela instalação dos respectivos 'Drivers' e SDK.

No entanto, a captação e o processamento de imagens em simultaneo com as restantes funções de controlo reveluo-se um desafio dificil de superar utilizando apenas o Raspberry PI 3, pelo que foi explorada a possibilidade de separar a captação da imagem e o controlo de baixo nível do controlo da alto nivel, instalando o ROS em dois locais, comprocessamento independente e comunicação pela rede LAN.

Foram assim estudadas as seguintes hipotese de locais de processamento, admitindo que a captação de imagens se faria sempre ao nível do 'Raspberry PI 3':
- [Raspberry PI3](#Processamento-da-Imagem-no-Raspberry-PI-3)
- [Raspberry PI 4](#Processamento-da-Imagem-no-Raspberry-PI-4)
- [PC Portatil]()
- [Carta Nvidia Jetson Nano]()

### Processamento da Imagem no Raspberry PI 3
