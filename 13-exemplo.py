import pytesseract
import numpy as np
import cv2
from pytesseract import Output
from PIL import ImageFont, ImageDraw, Image

fonte = 'Fontes/calibri.ttf'

img = cv2.imread('imagens/caneca.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#cv2.imshow("Imagem", rgb)
#cv2.waitKey(0)

config_tesseract = '--tessdata-dir tessdata --psm 11'
resultado = pytesseract.image_to_data(rgb, config=config_tesseract, lang='eng', output_type=Output.DICT)
print(resultado)

min_conf = 40

def escreve_texto(texto, x, y, img, fonte, tamanho_texto=32):
    fonte = ImageFont.truetype(fonte, tamanho_texto)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((x, y - tamanho_texto), texto, font= fonte)
    img = np.array(img_pil)

    return img

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
        texto = resultado['text'][i]
        if not texto.isspace() and len(texto) > 0:
            x, y, img = caixa_texto(resultado, img_copia)
            print(x, y)
            img_copia = escreve_texto(texto, x, y, img_copia, fonte)
cv2.imshow("Imagem", img_copia)
cv2.waitKey(0)
