import math

def calcular_coste(a, b, k):
    g = math.gcd(a, b)
    if max(a // g, b // g) <= k:
        print( max(a // g, b // g))
        return 1
    return 2

t = int(input())
for _ in range(t):
    a, b, k = map(int, input().split())
    print(calcular_coste(a, b, k))
