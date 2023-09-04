import os
import cv2
import numpy as np

from utils import *


# Inicialização
image_path = 'disco_hue.png'
# image_path = 'carro_azul.png'
# image_path = 'carro_vermelho.jpg'

m = ler(0, 359)
x = ler(0, 179)

lower_abs = (m - x) // 2  # Correção de valores para 8 bits
upper_abs = (m + x) // 2  # Correção de valores para 8 bits

lower_aux = max(lower_abs, 0)  # Limite inferior da faixa padrao
upper_aux = min(upper_abs, 179)  # Limite superior da faixa padrao
    

if not os.path.isfile(image_path):
    print("Imagem não encontrada!")
    exit()

original_image = cv2.imread(image_path)
hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
hsv_channel = hsv_image[:, :, 0]


# Processamento
if lower_abs < 0:  # Caso onde faixa de valores passa negativamente de 0
    lim_abs = lower_abs % 180  # Limite inferior ou superior da faixa excecao
    hsv_channel = \
        invert_range(hsv_channel, lim_abs, 179, -1)  # Inverter faixa excecao
    hsv_channel = \
        invert_range(hsv_channel, lower_aux, upper_aux)  # Inverter faixa padrao

elif upper_abs > 179:  # Caso onde faixa de valores passa de 179
    lim_abs = upper_abs % 180  # Limite inferior ou superior da faixa excecao
    hsv_channel = \
        invert_range(hsv_channel, 0, lim_abs)  # Inverter faixa excecao
    hsv_channel = \
        invert_range(hsv_channel, lower_aux, upper_aux, -1)  # Inverter faixa padrao
    
else:  # Caso onde somente faixa padrao possui valores
    mask_lower = cv2.inRange(  # Parte da faixa padrao < 89
        hsv_channel, lower_abs, min(upper_abs, 89))
    mask_upper = cv2.inRange(  # Parte da faixa padrao >= 90
        hsv_channel, max(lower_abs, 90), upper_abs)
    hsv_channel[mask_lower > 0] = \
        hsv_channel[mask_lower > 0] + 90 # Inverter faixa padrao < 89
    hsv_channel[mask_upper > 0] = \
        hsv_channel[mask_upper > 0] - 90 # Inverter faixa padrao >= 90


# Finalização
hsv_image[:, :, 0] = hsv_channel
rgb_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

cv2.imshow('New Image', rgb_image)
cv2.imshow('Original Image', original_image)

cv2.imwrite('new_image.png', rgb_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
