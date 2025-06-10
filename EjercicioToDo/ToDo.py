password = 1234
tareas = []

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
        print("3. Administrar tareas")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            nueva_password = int(input("Ingrese su nueva contraseña: "))
            password = nueva_password
            print("Contraseña cambiada exitosamente.")

        elif opcion == '2':
            print("Sesión cerrada exitosamente.\n")
            break

        elif opcion == '3':
            while True:
                print("\n--- ADMINISTRADOR DE TAREAS ---")
                print("1. Ver tareas")
                print("2. Agregar tarea")
                print("3. Marcar tarea como completada")
                print("4. Eliminar tarea")
                print("5. Volver al menú principal")
                tarea_opcion = input("Seleccione una opción: ").strip()

                if tarea_opcion == "1":
                    if not tareas:
                        print("No hay tareas.")
                    else:
                        print("\nTareas:")
                        for i, tarea in enumerate(tareas):
                            print(f"{i + 1}. {tarea}")

                elif tarea_opcion == '2':
                    nueva_tarea = input("Ingrese la nueva tarea: ").strip()
                    tareas.append(nueva_tarea)
                    print("Tarea agregada exitosamente.")

                elif tarea_opcion == '3':
                    if not tareas:
                        print("No hay tareas para marcar.")
                    else:
                        for i, tarea in enumerate(tareas):
                            print(f"{i + 1}. {tarea}")
                        num = int(input("Ingrese el número de la tarea completada: "))
                        if 1 <= num <= len(tareas):
                            tareas[num - 1] += " ✔️"
                            print("Tarea marcada como completada.")
                        else:
                            print("Número inválido.")

                elif tarea_opcion == '4':
                    print('Deseas volver al menu?')
                    confirmacionelim = input("s/n:").strip()
                    if confirmacionelim == "n":
                        if not tareas:
                            print("No hay tareas para eliminar.")
                        else:
                            for i, tarea in enumerate(tareas):
                                print(f"{i + 1}. {tarea}")
                            num = int(input("Ingrese el número de la tarea a eliminar: "))
                            if 1 <= num <= len(tareas):
                                tareas.pop(num - 1)
                                print("Tarea eliminada.")
                            else:
                                print("Número inválido.")
                    else:
                        print("Regresando al menú de tareas...")

                elif tarea_opcion == '5':
                    break

                else:
                    print("Opción inválida. Intenta de nuevo.")


        else:
            print("Opción inválida. Intenta de nuevo.")