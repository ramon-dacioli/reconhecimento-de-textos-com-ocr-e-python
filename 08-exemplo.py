import pytesseract
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('imagens/livro01.jpg')

# Exibir imagem com Matplotlib
plt.imshow(img)
plt.axis('off')  # Oculta os eixos (opcional)
plt.show()       # Mostra a imagem