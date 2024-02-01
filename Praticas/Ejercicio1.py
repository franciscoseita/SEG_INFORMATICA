from cryptography.fernet import Fernet

def descifrar_con_clave_existente():
    # Usuario ingresa la clave en formato base64
    clave_usuario = input("Ingrese la clave (en formato base64): ").encode()

    # Usuario ingresa el mensaje encriptado
    mensaje_encriptado_usuario = input("Ingrese el mensaje encriptado: ").encode()

    # Instancia de Fernet con la clave proporcionada por el usuario
    f = Fernet(clave_usuario)

    # Descifrar Mensaje
    try:
        mensaje_descifrado = f.decrypt(mensaje_encriptado_usuario)
        print("\nMensaje Descifrado:")
        print(mensaje_descifrado.decode())
    except Exception as e:
        print("Error al descifrar el mensaje:", str(e))

def encriptar_con_nueva_clave():
    # Generar una nueva clave
    clave_nueva = Fernet.generate_key()
    print("Nueva clave generada:", clave_nueva.decode())

    # Instancia de Fernet con la nueva clave generada
    f = Fernet(clave_nueva)

    # Usuario ingresa el mensaje
    mensaje_usuario = input("Ingrese el mensaje que desea encriptar: ")

    # Encriptación del mensaje
    try:
        mensaje_encriptado = f.encrypt(mensaje_usuario.encode())
        print("\nMensaje Encriptado:")
        print(mensaje_encriptado.decode())
    except Exception as e:
        print("Error al encriptar el mensaje:", str(e))

# Menú de opciones
print("Seleccione una opción:")
print("1. Descifrar mensaje con clave existente")
print("2. Encriptar mensaje con nueva clave")

opcion = input("Ingrese el número de la opción deseada (1 o 2): ")

if opcion == "1":
    descifrar_con_clave_existente()
elif opcion == "2":
    encriptar_con_nueva_clave()
else:
    print("Opción no válida. Por favor, ingrese 1 o 2.")
