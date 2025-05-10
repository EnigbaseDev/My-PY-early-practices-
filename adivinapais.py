
pais = str(input('Ingrese el nombre de su pais:')).strip().lower()
# El strip el para que si pone solo espacios, se borren y lo lea asi ("")
print(pais)

if pais == '':
    print('No ingresaste un pais valido')
# Cuando vea ciclos cierre aqui, si esta se cumple.

else:  
    if pais == "colombia":
        print('Buena eleccion, Colombia es un gran país.')

    elif pais == 'argentina':
        print('Interesante elección, Che')
    elif pais == 'brasil':
        print('Interesante elección, Monkey')
    elif pais == 'mexico':
        print('Interesante elección, one tak?')   
    else:
        print('Interesante eleccion, no lo conozco pero esta bien')