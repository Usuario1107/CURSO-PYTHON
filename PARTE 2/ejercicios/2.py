# pedir un numero y mostar los numero primos que hay hasta ese numero

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True

numeros = int(input("number: "))
primos = []

for i in range(2,numeros+1):
    if es_primo(i):
        primos.append(i)

print(primos)