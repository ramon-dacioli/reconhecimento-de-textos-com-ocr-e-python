import pytesseract
import numpy as np
import cv2

img = cv2.imread('imagens/teste01.jpg')
#cv2.imshow("Imagem", img)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow("Imagem", rgb)

#cv2.waitKey(0)

texto = pytesseract.image_to_string(rgb)

print(texto)

