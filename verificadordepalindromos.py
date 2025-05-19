import string

def es_palindromo(frase):
    # Quitar espacios y signos de puntuación, pasar a minúsculas
    frase_limpia = frase.lower()
    for char in string.punctuation + " ":
        frase_limpia = frase_limpia.replace(char, "")

    # Comparar frase con su reverso
    return frase_limpia == frase_limpia[::-1]

texto = input("Escribe una frase: ")
if es_palindromo(texto):
    print("¡Es un palíndromo!")
else:
    print("No es un palíndromo.")
