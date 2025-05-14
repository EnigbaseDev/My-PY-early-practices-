
monto = float(input('Ingrese el monto inicial de su prestamo:'))
interes = float(input('Ingrese el interes anual del prestamo:'))
años = int(input('Ingrese los años que durara el prestamo:'))

if monto <= 0 or interes <= 0 or años < 1:
    print('Error en los datos ingresados')
    if monto <= 0:
        print('El monto debe ser mayor que 0')
    if interes <= 0:
        print('La taza de interes no puede ser negativa o igual a 0')
    if años < 1:
        print('El prestamo debe ser de minimo 1 año de duracion')
    exit()

interesporcentual = interes/100

total_a_pagar = monto*(1+interesporcentual)**años

print('El total a pagar al final del prestamo sera de:',total_a_pagar)
0