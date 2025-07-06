import pytesseract
import numpy as np
import cv2
from pytesseract import Output

img = cv2.imread('imagens/teste_manuscrito_01.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("Imagem", rgb)
#cv2.waitKey(0)

config_tesseract = '--tessdata-dir tessdata'
resultado = pytesseract.image_to_data(rgb, config=config_tesseract, lang='por', output_type=Output.DICT)
print(resultado)

min_conf = 40

def caixa_texto(resultado, img, cor = (255,100,0)):
    x = resultado['left'][i]
    y = resultado['top'][i]
    w = resultado['width'][i]
    h = resultado['height'][i]

    cv2.rectangle(img, (x, y), (x + w, y + h), cor, 2)

    return x, y, img

img_copia = rgb.copy()
for i in range(0, len(resultado['text'])):
    confianca = int(resultado['conf'][i])
    if confianca > min_conf:
        x, y, img = caixa_texto(resultado, img_copia)
        print(x, y)
        texto = resultado['text'][i]
        cv2.putText(img_copia, texto, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0,0,255))
cv2.imshow("Imagem", img_copia)
cv2.waitKey(0)
