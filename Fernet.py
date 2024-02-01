#Cifrado Fernet

#Importar Fernet de pip install cryptography
from cryptography.fernet import Fernet
#Generar la clave
clave=Fernet.generate_key()
#instancia fernet
f = Fernet(clave)
#Encriptacion del mensaje
print("Mensaje Inicial: Mensaje Secreto \n")
print("Mensaje Encriptada:")
token = f.encrypt(b'Mensaje Secreto')
print(token)
print("\n")
#Decifrar Mensaje
print("Mensaje Descifrada:")
des = f.decrypt(token)
print(des)
