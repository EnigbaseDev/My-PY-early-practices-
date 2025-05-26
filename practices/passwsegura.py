

password = input("Ingresa tu contraseña: ")

simbolos = "!@#$%^&*()_-+=<>?/\\|{}[]"

tiene_longitud = len(password) >= 8
tiene_mayus = any(char.isupper() for char in password)
tiene_minus = any(char.islower() for char in password)
tiene_num = any(char.isdigit() for char in password)
tiene_simbolo = any(char in simbolos for char in password)

if tiene_longitud and tiene_mayus and tiene_minus and tiene_num and tiene_simbolo:
    print("Contraseña segura.")
else:
    print("Contraseña insegura. Revisa los siguientes puntos:")
    if not tiene_longitud:
        print("- Debe tener al menos 8 caracteres.")
    if not tiene_mayus:
        print("- Debe contener al menos una letra mayúscula.")
    if not tiene_minus:
        print("- Debe contener al menos una letra minúscula.")
    if not tiene_num:
        print("- Debe contener al menos un número.")
    if not tiene_simbolo:
        print("- Debe contener al menos un símbolo especial.")
