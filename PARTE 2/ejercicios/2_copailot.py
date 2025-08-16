# Pedir un número y mostrar los números primos hasta ese número

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):  # Solo hasta la raíz cuadrada
        if numero % i == 0:
            return False
    return True

numeros = int(input("number: "))
primos = [i for i in range(2, numeros + 1) if es_primo(i)]  # Lista por comprensión

print(primos)