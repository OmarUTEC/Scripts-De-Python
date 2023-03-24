import random
import string

# Definimos la longitud máxima de la contraseña
longitud_maxima = 25
longitud_minima = 20

# Definimos los caracteres que se usarán para generar la contraseña
caracteres = string.ascii_letters + string.digits + string.punctuation

# Pedimos al usuario cuántas contraseñas quiere generar
num_contraseñas = int(input("¿Cuántas contraseñas quieres generar? "))

# Generamos las contraseñas y las guardamos en un archivo de texto
with open("contraseñas.txt", "w") as archivo:
    for i in range(num_contraseñas):
        longitud = random.randint(longitud_minima, longitud_maxima)
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        archivo.write(contraseña + "\n")
        print("Contraseña #" + str(i+1) + ": " + contraseña)
