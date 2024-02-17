#Pratica de Algoritmo RSA
#Francisco Seita 14/02/2024

#imports
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
print("dA:", dA, "\n")

dB= Crypto.Util.number.inverse(e, phiB)
print("dA:", dB, "\n")

#Ciframos el mensaje
msg='Hola Mundo'
print("Mensaje Original: " ,msg,"\n")
print("Longitud del mensaje en bytes:", len(msg.encode('utf-8')))

#Convertir el mensaje a numero
m=int.from_bytes(msg.encode('utf-8'),byteorder='big')
print("Mensaje convertido en entero:",m,"\n")

#Cifrar el mensaje
c=pow(m,e,nB)
print("Mensaje Cifrado:",c,"\n")

#Decifrar el mensaje
des=pow(c,dB,nB)
print("Mensaje Decifrado:",des,"\n")

#Covertimos el mensaje de numero a texto
msg_final =int.to_bytes(des,len(msg),byteorder='big').decode('utf-8')
print("Mensaje Final:" ,msg_final,"\n")


