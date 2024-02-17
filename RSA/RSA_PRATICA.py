import hashlib
import Crypto.Util.number

#Numero de bits
bits = 1024
#Obtener los primos para alice y bob
pA=Crypto.Util.number.getPrime(bits,randfunc=Crypto.Random.get_random_bytes)
print("aP:",pA,"\n")
qA=Crypto.Util.number.getPrime(bits,randfunc=Crypto.Random.get_random_bytes)
print("qA:",qA,"\n")
pB=Crypto.Util.number.getPrime(bits,randfunc=Crypto.Random.get_random_bytes)
print("aP:",pB,"\n")
qB=Crypto.Util.number.getPrime(bits,randfunc=Crypto.Random.get_random_bytes)
print("qA:",qB,"\n")
#Primera parte de la llave publica de Alice y Bob
nA= pA *qA
print("nA:", nA, "\n")
nB= pB *qB
print("nA:", nB, "\n")
#Calcular el indicador de euler phi
phiA=(pA-1)*(qA-1)
print("phiA:", phiA, "\n")
phiB=(pB-1)*(qB-1)
print("phiB:", phiB, "\n")
#POR RAZONES DE EFICIENCIA USAREMOS EL NUMERO 4 DE FERNET, 65537, DEBIDO A QUE ES UN PRIMO LARDO Y NO ES DE POTENCIA 2
e=65537
#Calcular llave privada de alice y bob
dA= Crypto.Util.number.inverse(e, phiA)
dB= Crypto.Util.number.inverse(e, phiB)

message = "HOLA MUNDO"
message_hash = hashlib.sha256(message.encode()).digest()

# Convert hash to integer
hash_int = int.from_bytes(message_hash, byteorder='big')
print("Mensaje hash int:", hash_int, "\n")

c=pow(hash_int,dA,nA)
print("Mensaje Cifrado:",c,"\n")

des=pow(c,e,nA)
print("Verificacion de hash int:",des,"\n")

if hash_int==des:
    print("El Mensaje fue firmado por alice")
else:
    print("El mensaje no fue firmado por alice")



