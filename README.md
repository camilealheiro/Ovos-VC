# Pesquisa Ovos + Visão computacional
## Bibliotecas recomendadas para instalação
- OpenCV
- pyrealsense2
- PyTorch
- Numpy
- Sklearn
- Pillow
- Matplotlib
- Pandas

## Códigos Utilizados
### Wrapper3.py
Esse código foi utilizado para transformar os vídeos de profundidade em formato .bag para uma imagem 16 bits em formato .png.  
Como a base desse código é um código exemplo da utilizando a librealsense, para executá-lo, é necessário o uso do cdm com o seguinte comando:
```
python wrapper3.py -i video.bag
```
Após a execução, será gerada uma imagem 16 bits em preto e branco, como a seguinte:
![Picture1_position1](https://github.com/camilealheiro/Ovos-VC/assets/91702532/cc4d0b1f-8eb7-4667-b26a-533cac3b9fe0)   
**OBS**   
Os vídeos de profundidade podem estar gravados em dois tipos de resolução (1280 x 720 ou 640 x 480). Dependendo do tipo de resolução do vídeo, é necesário leves modificações no código, sendo elas:   
- **Troca da especificação da resolução**
```
#Para 1280 x 720
config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
#Para 640 x 480
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 15)
```
- **Troca da largura e altura da imagem que será escrita**
```
IMAGE_WIDTH = 1280
IMAGE_HEIGHT = 720
#OU
IMAGE_WIDTH = 640
IMAGE_HEIGHT = 480
```

### segmentacao.py
Esse código irá fazer o recorte semi-automático dos ovos em cada imagem PNG.   
- Ao rodá-lo, ele irá mostrar a imagem de profundidade escolhida e escrita como caminho no parâmetro da função `limiar_func()`;
- Após apertar qualquer tecla, a mesma imagem irá aparecer, porém para escolher o fim da primeira fileira de ovos na bandeja, dessa forma fazendo um recorte automático da fileira escolhida onde será aplicada a limiarização;
- A escolha da coordenada do fim da fileira escolhida irá gerar uma pergunta, mostrada no terminal, para confirmar se o recorte saiu da forma planejeda, sendo necessário a escrita de "s", para se a segmentação está correta, ou "n" para escolher a coordenada novamente;
- Após o recorte correto da fileira de ovos será feita a limiarização dos ovos, a fim de ser possível detectar os contornos de cada ovo fazendo com que seja recortado adequadamente. A limiarização pode ser feita com o auxílio da trackbar ou digitando "e" e escrevendo o valor do limiar no terminar (o método de utilizar o "e" pode ser feito quantas vezes necessitar);
- Após a escolha do limiar será pedido o número do ovo mais a esquerda da fileira, dessa forma, após detectar o contorno dos ovos, os mesmos serão salvos como PNG de 16 bits com seus respectivos números.
- Todo esse ciclo irá se repetir até a terceira fileira ser finalizada.

***OBS***
O código é 90% efetivo, portanto é necessário verificar se o recorte dos ovos foi salvo corretamente, coisas como as seguintes ainda podem acontecer:
- Identificação de contornos que não são os ovos;
- Limiarização não funcionar na fileira toda (nesses casos é necessário o recorte manual, por meio do coordenadas.py, do ovo que não foi salvo).   
***Ambas as situações acontecem muito pouco***

### Coordenadas.py
Esse código faz com que seja mostrada as coordenadas desejadas da imagem após clicar no lugar de interesse na imagem.  
Foi utilizado para ajudar na segmentação manual individual dos ovos.  
Para executar é necessário apenas rodá-lo na IDE de preferência (usei o VS Code).

### Crop.py
O Crop irá fazer o recorte em si dos ovos, utilizando as coordenadas de cada ovo nas imagens tiradas com a ajuda do `coordenadas.py`.  
As coordenadas de recorte cada ovo foi armazenada em uma planilha `Recorte ovos 14 dias`, contendo coordenadas desde o ovo 399 até o ovo 598 (14 dias).  
O recorte é feito utilizando as coordenadas de X e Y iniciais e finais da área desejada para recorte e para executar o código é apenas preciso modificar no código o X e Y finais e iniciais (como descritos na planilha) e rodá-lo na IDE de preferência (usei o VS Code).

### Normalize.py
Após o recorte individual dos ovos, foi discutida a necessidade de uma normalização das imagens devido a possíveis diferenças de distância na captação das imagens de profundidade.  
O normalize.py realiza essa normalização que pode ser feita antes ou depois das segmentações, basta mudar o diretório desejado e a quantidade de elementos que serão normalizados.  
A imagem final é novamente salva em um PNG de 16 bits, como o exemplo abaixo:  
![ovo399](https://github.com/camilealheiro/Ovos-VC/assets/91702532/a756c5df-c836-414e-a901-501ef8c2390e)

### CNNmodel4.ipynb
Nesse Jupyter Notebook foi feito o início da implementação do modelo de regressão utilizando Rede Neural Convolucional.  
Nele foi feita a CNN inicial, o dataset próprio, o treino, o teste e as métricas de avaliação.  
Como dataset, foi utilizado as imagens das segmentações individuais normalizadas dos ovos de 14 dias, divididas em folders de teste e treino, e as informações das medidas dos ovos que queremos prever que estão nas planilhas `test.csv` e `train.csv`.


