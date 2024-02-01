#Pratica 1

#importamos las librerias
from Crypto.Util import number
import random 

#Ejercicio1 Numero aleatorio de 256 BITS
print("Ejercicio 1 - Obtener un numero aleatorio de 256 Bits usando la funcion random",'\n',random.getrandbits(256), '\n')

#Ejercicio2 Buscar Numeros Primos
print("Ejercicio 2 Buscar Numeros Primos \n")
i = 0
while(True):
    i = i + 1
    j = random.getrandbits(1024)
    esPrimo = number.isPrime(j)
    if(esPrimo):
        print("En la iteracion:",i,"se encontro el primo:", j, "\n")
        break

#Ejercicio3 Inverso Multiplicado Cifrado
def inversoMultiplicativo(x,y):
    print("Ejercicio3- El inverso Multiplicativo del numero x:", "\n",x,"\n","y el numero y:","y el numero y:","\n",y,"\n","es: ","\n", number.inverse(x,y),"\n" )
       
a = random.getrandbits(1024)
b = random.getrandbits(1024)
inversoMultiplicativo(a,b)

#Ejercicio 4
#Potencia de un numero 2 
a=2 
b = random.getrandbits(256)
c= j

def potencia(x,y,z):
    print("Ejercicio 4 - la potencia de x a la y mod z es: ", "\n", pow(x,y,z))
potencia(a,b,c)


