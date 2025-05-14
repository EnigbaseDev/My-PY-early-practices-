
password = 1234

while True:
    intentos = 0
    user = input("Ingrese su usuario: ").lower().strip().replace(' ', '')

    while user != 'admin' and intentos < 3:
        print('Usuario Incorrecto.')
        user = input('Ingrese su usuario nuevamente: ').lower().strip().replace(' ', '')
        intentos += 1

    if intentos >= 3:
        print("Acceso bloqueado (Intentaste demasiadas veces)\n")
        while True:
            opcion = input("¿Desea intentar de nuevo? (s/n): ").lower().strip()
            if opcion == 'n':
                print("Saliendo del programa. Hasta luego.")
                exit()
            elif opcion == 's':
                print("Reiniciando intento...\n")
                break
            else:
                print("Opción inválida. Escribe 's' para sí o 'n' para no.")
        continue

    # Usuario correcto, pide contraseña
    intentos = 0
    password_ingresado = int(input("Ingrese su contraseña: "))

    while password_ingresado != password and intentos < 2:
        print("Contraseña Incorrecta. Inténtelo nuevamente.")
        password_ingresado = int(input("Ingrese su contraseña: "))
        intentos += 1

    if password_ingresado != password:
        print("Acceso bloqueado (Intentaste demasiadas veces)\n")
        while True:
            opcion = input("¿Desea intentar de nuevo? (s/n): ").lower().strip()
            if opcion == 'n':
                print("Saliendo del programa. Hasta luego.")
                exit()
            elif opcion == 's':
                print("Reiniciando intento...\n")
                break
            else:
                print("Opción inválida. Escribe 's' para sí o 'n' para no.")
        continue

    # Si el acceso esta bien
    print("Bienvenido administrador.\n")

    # Menu
    while True:
        print("\n--- MENÚ ---")
        print("1. Cambiar contraseña")
        print("2. Cerrar sesión")
        opcion = input("Seleccione una opción (1 o 2): ").strip()

        if opcion == '1':
            nueva_password = int(input("Ingrese su nueva contraseña: "))
            password = nueva_password
            print("Contraseña cambiada exitosamente.")

        elif opcion == '2':
            print("Sesión cerrada exitosamente.\n")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")