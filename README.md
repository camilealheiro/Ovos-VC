# Pesquisa Ovos + Visão computacional
## Bibliotecas recomendadas para instalação
- OpenCV
- pyrealsense2
- PyTorch
- Numpy
- Sklearn
- Pillow
- Matplotlib

## Códigos Utilizados
### Wrapper3.py
Esse código foi utilizado para transformar os vídeos de profundidade em formato .bag para uma imagem 16 bits em formato .png.  
Como a base desse código é um código exemplo da utilizando a librealsense, para executá-lo, é necessário o uso do cdm com o seguinte comando:
```
python wrapper3.py -i video.bag
```
Após a execução, será gerada uma imagem 16 bits em preto e branco, como a seguinte:
![Picture1_position1](https://github.com/camilealheiro/Ovos-VC/assets/91702532/cc4d0b1f-8eb7-4667-b26a-533cac3b9fe0)

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


