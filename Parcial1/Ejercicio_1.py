from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
import hashlib



# Generar las llaves
key_size = 2048
alice_key = RSA.generate(key_size)
bob_key = RSA.generate(key_size)

# Imprimir las llaves publicas y privadas
print("Alice's public key: ", alice_key.publickey().export_key().hex() , "\n")
print("Alice's private key: ", alice_key.export_key().hex(),"\n")
print("Bob's public key: ", bob_key.publickey().export_key().hex(),"\n")
print("Bob's private key: ", bob_key.export_key().hex(),"\n")

#mensaje
message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed commodo, velit eget laoreet tempus, nisi nibh euismod nibh, vel consectetur nunc nunc eget nunc. Sed bibendum ultrices ante, non laoreet ex egestas ut. Curabitur vestibulum aliquam leo. Sed auctor, magna a ullamcorper laoreet, dolor quam porttitor sapien, a accumsan nisi nibh sed velit. Sed elementum, velit eget laoreet tempus, nisi nibh euismod nibh, vel consectetur nunc nunc eget nunc. Sed bibendum ultrices ante, non laoreet ex egestas ut. Curabitur vestibulum aliquam leo. Sed auctor, magna a ullamcorper laoreet, dolor quam porttitor sapien, a accumsan nisi nibh sed velit. Sed elementum, velit eget laoreet tempus, nisi nibh euismod nibh, vel consectetur nunc nunc eget nunc. Sed bibendum ultrices ante, non laoreet ex egestas ut. Curabitur vestibulum aliquam leo. Sed auctor, magna a ullamcorper laoreet, dolor quam porttitor sapien, a accumsan nisi nibh sed velit. Sed elementum, velit eget laoreet tempus, nisi nibh euismod nibh, vel consectetur nunc nunc eget nunc. Sed bibendum ultrices ante, non laoreet ex egestas ut. Curabitur vestibulum aliquam leo. Sed auctor, magna a ullamcorper laoreet, dolor quam porttitor sapien, a accumsan nisi nibh sed velit. Sed elementum, velit eget laoreet tempus, nisi nibh euismod nibh, vel consectetur nunc nunc eget nunc. Sed bibendum ultrices ante, non laoreet ex egestas ut. Curabitur vestibulum aliquam leo. Sed auctor, magna a ullamcorper laoreet, dolor quam porttitor sapien, a accumsan nisi nibh sed velit."

# Generar el hash del mensaje
h_M = hashlib.sha256(message.encode()).hexdigest()

# Division del mensaje 
message_parts = [message[i:i+128] for i in range(0, len(message), 128)]

# Encriptacion por partes con la llave publica de bob
encrypted_parts = []
for part in message_parts:
    cipher = PKCS1_OAEP.new(bob_key.publickey())
    encrypted_part = cipher.encrypt(part.encode())
    encrypted_parts.append(encrypted_part)

# Decrypt por partes con llave privada de bob
decrypted_parts = []
for part in encrypted_parts:
    cipher = PKCS1_OAEP.new(bob_key)
    decrypted_part = cipher.decrypt(part).decode()
    decrypted_parts.append(decrypted_part)

# Juntas las partes separadas
decrypted_message = "".join(decrypted_parts)

# Generar el hash del mensaje
h_M_prime = hashlib.sha256(decrypted_message.encode()).hexdigest()

print("Hash del mensaje original (h(M)):", h_M,"\n")
print("hash del mensaje decryted (h(M')):", h_M_prime,"\n")

#Verificar que los mensajes son iguales
print("Original message:", message,"\n")
print("Decrypted message:", decrypted_message,"\n")

# Comparar hashes
if h_M == h_M_prime:
    print("Hashes son iguales, message es autentica","\n")
else:
    print("Hashes no son iguales, message no es autentica","\n")