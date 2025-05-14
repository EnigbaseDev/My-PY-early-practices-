
contact1 = (input('Ingrese el nombre del contacto 1:')).lower()
consulta1 = int(input(f'Ingrese el numero de {contact1}: '))
num1 = consulta1

contact2 = (input('Ingrese el nombre del contacto 2:')).lower()
consulta2 = int(input(f'Ingrese el numero de {contact2}: '))
num2 = consulta2

contact3 = (input('Ingrese el nombre del contacto 3:')).lower()
consulta3 = int(input(f'Ingrese el numero de {contact3}: '))
num3 = consulta3

datos = {contact1:num1,contact2:num2,contact3:num3}

consulta = (input('A quien deseas llamar?:')).lower()

if consulta in datos:
    llamada = datos[consulta]
    print('Llamando al', llamada)
else:
    print('Este contacto no esta guardado')

