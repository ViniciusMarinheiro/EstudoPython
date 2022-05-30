import pyshorteners

# URL Orginal
url = 'Digite aqui a URL ou texto'

# Carrega a lib
s = pyshorteners.Shortener()

# Gera a URL encurtada
shortUrl = s.tinyurl.short(url)

# Resultado
print(f'URL Encurtada: {shortUrl}')