import cv2
import numpy as np

def ler(x, y):
    while True:
        z = int(input(f"Digite um numero de {x}-{y}: "))
        if x <= z <= y:
            break

    return z

def invert_range(channel, lower, upper, sign=1):
    mask = cv2.inRange(channel, lower, upper)
    channel[mask > 0] = channel[mask > 0] + sign * 90

    return channel
