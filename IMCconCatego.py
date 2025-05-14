
peso = float(input('Ingrese su Peso:'))
altura = float(input('Ingrese su Altura:'))
IMC = peso/(altura**2)
if IMC<18.5:
    categoria ='Flacow'
elif 18.5<=IMC<=24.9:
    categoria ='Saludable'
elif 25<=IMC<=29.9:
    categoria='Casco'
elif IMC >=30:
   categoria='Tomas?'
print('Su IMC es de:',IMC)
print('Su categoria es:',categoria)