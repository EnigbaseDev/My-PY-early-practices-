
import random
num = random.randint(1,10)

adivinar = int(input('Adivina el numero entre 1 y 10, ingresa tu numero:'))

while adivinar != num:
    if abs(adivinar - num) == 1:
        print('Estas muy cerca, pero no es ese')
    else:
        print('Ese no es el numero, Intenta de nuevo.')
    adivinar = int(input("Intenta otra vez:"))
    
print ('Felicidades, adivinaste el numero')