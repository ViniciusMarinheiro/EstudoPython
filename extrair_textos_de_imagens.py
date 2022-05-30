import easyocr

# Define o idioma a ser usado
reader = easyocr.Reader(['pt'])

# Carrega e faz a leitura da imagem
resultados = reader.readtext(r'D:\vinic\Pictures\Capturar.PNG', paragraph=False)

# Mostra os resultados
for resultado in resultados:
    print(resultado[1])