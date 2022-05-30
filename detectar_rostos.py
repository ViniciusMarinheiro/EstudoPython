import cv2


# Carrega modelo
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Carrega imagem
img = cv2.imread("pessoas2.jpg")

# Converte para escala em cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecta rostos
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Desenha um retangulo no rosto detectado
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0,), 2)

# Mostra o resultado
cv2.imshow('img', img)
cv2.waitKey()