import smtplib

# Datos del correo electrónico
destinatario = 'xxxxxxx.com'
asunto = 'Prueba'
cuerpo = 'Esto es una prueba de Hackeo'

# Datos de la cuenta de Gmail
usuario = 'xxxxxxxxxx@gmail.com'
password = 'xxxxxx'

# Crear el objeto del servidor SMTP de Gmail
server = smtplib.SMTP('smtp.gmail.com', 587)

# Iniciar sesión en el servidor SMTP
server.starttls()
server.login(usuario, password)

# Crear el correo electrónico
mensaje = f'Subject: {asunto}\n\n{cuerpo}'

# Enviar el correo electrónico
server.sendmail(usuario, destinatario, mensaje)

# Cerrar la conexión con el servidor SMTP
server.quit()

print('Correo electrónico enviado exitosamente')
