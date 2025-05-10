

lista = [5, 2, 9, 1, 7, 9]

#ordenar
lista.sort()

#calcular la mediana
n = len(lista)
if n % 2 == 1:  # cantidad impar
    mediana = lista[n // 2]
else:  # cantidad par
    mediana = (lista[n//2 - 1] + lista[n//2]) / 2 # saco los dos datos de la mitad y hago promedio de estos 2

print('La mediana es:', mediana)