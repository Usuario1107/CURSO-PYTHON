def calcular_reparticion(p):
    return "YES" if p % 2 == 0 and p != 2 else "NO"

peso = int(input())
print(calcular_reparticion(peso))

