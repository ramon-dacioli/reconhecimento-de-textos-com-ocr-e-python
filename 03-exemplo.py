import pytesseract
import numpy as np
import cv2

img = cv2.imread('imagens/teste01.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
texto = pytesseract.image_to_string(rgb)
print(texto)


