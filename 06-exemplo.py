import pytesseract
import numpy as np
import cv2

img = cv2.imread('imagens/teste02.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("Imagem", rgb)
texto = pytesseract.image_to_string(rgb)
print(texto)

texto = pytesseract.image_to_string(rgb, lang='por')
print(texto)

config_tesseract = '--tessdata-dir tessdata'

texto = pytesseract.image_to_string(rgb, lang='por', config=config_tesseract)
print(texto)
