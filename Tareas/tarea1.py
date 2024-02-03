import random
import hashlib

def hex_to_int(hex_value):
    return int(hex_value, 16)

# 1. Encontrar un número primo p (usando tu valor en hexadecimal)
p_hex = "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF"  # tu valor hexadecimal
p = hex_to_int(p_hex)
g = 2

# 2. Generar las llaves privadas de Alice (A) y Bob (B)
a_private_key = random.getrandbits(256)
b_private_key = random.getrandbits(256)

# 3. Simular el intercambio de números entre Alice y Bob
A = pow(g, a_private_key, p)
B = pow(g, b_private_key, p)

# 4. Calcular la llave secreta "s"
s_alice = pow(B, a_private_key, p)
s_bob = pow(A, b_private_key, p)

# Verificar que las llaves secretas sean iguales usando SHA-256
hash_s_alice = hashlib.sha256(str(s_alice).encode()).hexdigest()
hash_s_bob = hashlib.sha256(str(s_bob).encode()).hexdigest()

print("Llave secreta de Alice:", s_alice)
print("Llave secreta de Bob:", s_bob)

if hash_s_alice == hash_s_bob:
    print("Las llaves secretas coinciden.")
else:
    print("Las llaves secretas no coinciden.")
