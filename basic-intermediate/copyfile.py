imagem = open("PYTHON/foto.jpg", "rb")
data = imagem.read()
imagem.close()

imagem_copia = open("PYTHON/foto_copia.pdf", "wb")
imagem_copia.write(data)
imagem_copia.close()