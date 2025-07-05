import pytesseract
import numpy as np
import cv2

img = cv2.imread('imagens/teste02.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("Imagem", rgb)
cv2.waitKey(0)

