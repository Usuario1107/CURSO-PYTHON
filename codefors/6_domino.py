def max_domino(m,n):
    return int((m * n) // 2)

m,n = map(int,input().split())
print(max_domino(m,n))