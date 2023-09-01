import os
import cv2
import numpy as np


# Inicialização
image_path = 'disco_hue.png'
m = 45
x = 90
teste2 = (m - x) // 2
teste3 = (m + x) // 2
lower_hue_range = max(teste2, 0)
upper_hue_range = min(teste3, 179)
if teste2 < 0:
    teste = teste2 % 180
else:
    teste = teste3 % 180
    

if not os.path.isfile(image_path):
    print("Imagem não encontrada!")
    exit()

original_image = cv2.imread(image_path)
hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)


# Processamento
mask = cv2.inRange(hsv_image, (lower_hue_range, 0, 0), (upper_hue_range, 255, 255))

if teste2 < 0:
    print(teste)
    mask1 = cv2.inRange(hsv_image, (teste, 0, 0), (179, 255, 255))
    hsv_image[mask1 > 0, 0] = hsv_image[mask1 > 0, 0] - 90
    hsv_image[mask > 0, 0] = (hsv_image[mask > 0, 0] + 90) % 180
else:
    print(teste)
    mask1 = cv2.inRange(hsv_image, (0, 0, 0), (teste, 255, 255))
    hsv_image[mask1 > 0, 0] = hsv_image[mask1 > 0, 0] + 90
    hsv_image[mask > 0, 0] = (hsv_image[mask > 0, 0] - 90) % 180


# Finalização
rgb_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

cv2.imshow('HSV Image', rgb_image)
cv2.imshow('Original Image', original_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
