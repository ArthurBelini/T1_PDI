import os
import cv2
import numpy as np

from utils import *


# Inicialização
image_path = 'disco_hue.png'

m = ler(0, 359)
x = ler(0, 180)

lower_abs = (m - x) // 2  # Correção de valores para 8 bits
upper_abs = (m + x) // 2  # Correção de valores para 8 bits

lower_aux = max(lower_abs, 0)  # Limite inferior da faixa padrao
upper_aux = min(upper_abs, 179)  # Limite superior da faixa padrao
    

if not os.path.isfile(image_path):
    print("Imagem não encontrada!")
    exit()

original_image = cv2.imread(image_path)
hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)


# Processamento
mask_abs = cv2.inRange(  # Faixa de valores padrao
    hsv_image, (lower_aux, 0, 0), (upper_aux, 255, 255))

if lower_abs < 0:  # Caso onde faixa de valores passa negativamente de 0
    low_up = lower_abs % 180  # Limite inferior ou superior da faixa excecao
    mask_aux = cv2.inRange(  # Mascara da faixa excecao
        hsv_image, (low_up, 0, 0), (179, 255, 255))
    hsv_image[mask_aux > 0, 0] = \
        hsv_image[mask_aux > 0, 0] - 90  # Inverter faixa excecao
    hsv_image[mask_abs > 0, 0] = \
        (hsv_image[mask_abs > 0, 0] + 90) % 180  # Inverter faixa padrao

elif upper_abs > 179:  # Caso onde faixa de valores passa de 179
    low_up = upper_abs % 180  # Limite inferior ou superior da faixa excecao
    mask_aux = cv2.inRange(  # Mascara da faixa excecao
        hsv_image, (0, 0, 0), (low_up, 255, 255))
    hsv_image[mask_aux > 0, 0] = \
        hsv_image[mask_aux > 0, 0] + 90  # Inverter faixa excecao
    hsv_image[mask_abs > 0, 0] = \
        (hsv_image[mask_abs > 0, 0] - 90) % 180  # Inverter faixa padrao
    
else:  # Caso onde somente faixa padrao possui valores
    hsv_image[mask_abs > 0, 0] = \
        (hsv_image[mask_abs > 0, 0] + 90) % 180  # Inverter faixa padrao


# Finalização
rgb_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

cv2.imshow('New Image', rgb_image)
cv2.imshow('Original Image', original_image)

cv2.imwrite('new_image.png', rgb_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
