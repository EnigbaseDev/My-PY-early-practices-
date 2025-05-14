
ellorax = {'name':'ellorax','año':2012,'genero':'fantasia'}
frozen = {'name':'frozen','año':2013,'genero':'hielo'}
eldelfin = {'name':'eldelfin','año':2002,'genero':'mar'}

peliculas = [ellorax,frozen,eldelfin]

consulta = str(input('que pelicula buscas?')).strip().lower().replace(' ', '')


if consulta == '':
  print('ingrese un nombre valido')


else:
  encontrado = False
  for pelicula in peliculas:
    if pelicula['name'] == consulta:
      print(f'Pelicula encontrada: Nombre: {pelicula['name']} Year: {pelicula['año']} Genero: {pelicula['genero']}')
      encontrado = True
      break

if not encontrado:
  print('Esta película no se encuentra en la lista: Error 404')
