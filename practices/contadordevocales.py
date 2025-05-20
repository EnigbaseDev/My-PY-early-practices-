frase = input("Ingrese una frase: ").lower()
contador = 0

for letra in frase:
    if letra in "aeiou":
        contador += 1

print(f"La frase contiene {contador} vocales.")
