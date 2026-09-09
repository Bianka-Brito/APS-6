from PIL import Image
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


#abrindo o caminho da imagem, pois no jupyter abriu direto mas no python não 
arquivo_atual = Path(__file__)
arquivo_atual.parent
pasta_src = arquivo_atual.parent
pasta_proj = pasta_src.parent
caminho_imagem = (pasta_proj/ "imagens"/ "originais"/ "queimadas"/ "queimada1.jpg")

#abrindo a imagem
imagem = Image.open(caminho_imagem)
imagem.show()

#largura e altura da imagem 
tamanho = imagem.size
print(tamanho)


#modo da imagem (RGB)
modo = imagem.mode
print(modo)

#descobrindo as cores de um pixel especifico para comparar area verde com queimadas 
pixel = imagem.getpixel((0,0))
print(pixel)

pixel2 = imagem.getpixel((100, 100))
print('Pixel área verde',pixel2)

pixel_queimada = imagem.getpixel((600, 200))
print('Pixel área queimada',pixel_queimada)

#transformar todos os pixels em matrizes com valores RGB
imagem_array = np.array(imagem)
print(imagem_array.shape) #formato da matriz (a,l,RGB)

#separando canal de cores 
vermelho = imagem_array[:,:,0]
verde = imagem_array[:,:,1]
azul = imagem_array[:,:,2]
print(vermelho.shape, verde.shape,azul.shape)

#isolando o vermelho
plt.imshow(vermelho, cmap='gray') #prepara a img 
plt.show() #mostra a img 

plt.imshow(vermelho) #prepara a img 
plt.show() #mostra a img 

#isolando o verde
plt.imshow(verde, cmap='gray') #prepara a img 
plt.show() #mostra a img 

plt.imshow(verde) #prepara a img 
plt.show() #mostra a img 

#isolando o azul
plt.imshow(azul, cmap='gray') #prepara a img 
plt.show() #mostra a img 

plt.imshow(verde) #prepara a img 
plt.show() #mostra a img 

imagem_cinza = imagem.convert('L') # L pois vamos trabalhar com a luminosidade
print(imagem_cinza.mode)
imagem_cinza.size
plt.imshow(imagem_cinza, cmap='gray')
plt.show()

imagem_cinza_array = np.array(imagem_cinza)
print(imagem_cinza_array.shape) #formato da matriz (a,l) #confirmamos que não tem mais RGB esta baseando na luminosidade

luminosidade_minima = imagem_cinza_array.min()
print(luminosidade_minima)

luminosidade_maxima = imagem_cinza_array.max()
print(luminosidade_maxima)

#criar um historiograma para analisar a distribuição dos valores da luminisidade e decidir a altura da mascara 
plt.hist(imagem_cinza_array.flatten())  #transformando a matriz em uma sequencia de valores
limite = 50 #iremos iniciar usando pixels a baixo de 50 como escuros para areas queimadas 
plt.axvline(limite, color='red', linestyle='--', linewidth=1)
plt.show()

#compara os pixels que tem menos luminosidade que o limite(50)
mascara = imagem_cinza_array < limite
plt.imshow(mascara, cmap='gray')
plt.show()