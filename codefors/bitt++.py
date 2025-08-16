N = int(input())
entradas = [input() for _ in range(N)]

def salida(listas):
    x=0
    for lista in listas:
        if lista == "++X" or lista == "X++":
            x += 1
        else:
            x -= 1
    return x

print(salida(entradas))
