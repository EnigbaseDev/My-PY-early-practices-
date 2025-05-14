
user = input("Ingrese su usuario:").lower().strip().replace(' ', '')
intentos = 0


while intentos < 3:
    if user != 'admin':
        print('Usuario Incorrecto')
        user = input('Ingrese nuevamente su user:').lower().strip().replace(' ', '')
        intentos += 1
    else:
        password = int(input("Ingrese su contraseña:"))
        while password != 1234 and intentos < 3:
            print("Contraseña Incorrecta, intentelo nuevamente")
            password = int(input("Ingrese su contraseña:"))
            intentos += 1
        if password == 1234:
            print("Bienvenido administrador")    
            break

if intentos >= 3:
    print ("Acceso bloqueado (Intentaste, demasiadas veces)")
