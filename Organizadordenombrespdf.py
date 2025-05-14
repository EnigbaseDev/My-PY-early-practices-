 
mylist =['Lucas', 'Valentina', 'Mateo', 'Isabella', 'Santiago', 'Camila',
          'Sebastián', 'Mariana', 'Nicolás', 'Gabriela', 'Samuel', 'Salomé',
          'Emiliano', 'Julieta', 'Daniel', 'Sara', 'Tomás', 'Antonia', 'Martín', 'Laura']

with open ('nombres', 'w') as file:
    for name in mylist:
       file.write(name + '\n')

with open ('nombres', 'r') as file:
    lectura = file.readlines()
    nombres = [nombre.strip() for nombre in lectura]
    nombres.sort()

print ('Nombres organizados:')

for nombre in nombres:
    print(nombre)
