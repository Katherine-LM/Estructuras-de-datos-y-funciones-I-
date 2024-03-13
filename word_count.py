with open("lorem_ipsum.txt", "r") as file:
    texto = file.read()

# Contar caracteres distintos
caracteres_distintos = set(texto)
num_caracteres_distintos = len(caracteres_distintos)

print(f"El número de caracteres distintos es: {num_caracteres_distintos}")

#contar el número de palabras distintas
palabras = texto.split(" ")
palabras_distintas = set(palabras)
num_palabras_distintas = len(palabras_distintas)

print(f"El número de palabras distintas es: {num_palabras_distintas}")



