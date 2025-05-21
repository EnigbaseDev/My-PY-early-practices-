
import string

#Crear Archivo

with open("texto.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola, este es un texto creado desde Python.\n")
    archivo.write("Segunda línea del tecto.\n")

# Leer archivo

with open("texto.txt", "r", encoding="utf-8") as file:
    texto = file.read()

# Limpiar texto

texto = texto.lower()
for simbolo in string.punctuation + "¿¡":
    texto = texto.replace(simbolo, "")

# Contar palabras

palabras = texto.split()
total_palabras = len(palabras)

conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

# Top 5 palabras mas comunes

top_5 = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:5]

# Mostrar resultados

print(f"\nTotal de palabras: {total_palabras}")
print("Top 5 palabras más frecuentes:")
for palabra, cantidad in top_5:
    print(f"- {palabra}: {cantidad}")

# Buscar palabra

buscar = input("\nIngresa una palabra para buscar: ").lower()
apariciones = conteo.get(buscar, 0)
print(f"La palabra '{buscar}' aparece {apariciones} veces.")
