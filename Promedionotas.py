
nota1 = int(input('Cual es el valor de la nota1?'))
nota2 = int(input('Cual es el valor de la nota2?'))
nota3 = int(input('Cual es el valor de la nota3?'))
nota4 = int(input('Cual es el valor de la nota4?'))
nota5 = int(input('Cual es el valor de la nota5?'))
resultado = (nota1 + nota2 + nota3 + nota4 + nota5)/5

print('tu promedio para esta materia es de:', resultado)

print('asi que en conclusion:')
if resultado >=3:
  print('Ganaste la materia')
else:
  print ('Perdiste la materia')