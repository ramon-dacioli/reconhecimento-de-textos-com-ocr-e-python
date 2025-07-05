import pytesseract
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('imagens/livro01.jpg')

print(pytesseract.image_to_osd(img))