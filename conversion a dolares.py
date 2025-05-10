
pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))

dolares = pesos * 0.00025 + soles * 0.28 + reais * 0.21

print('en dolares tienes:')
print(dolares)