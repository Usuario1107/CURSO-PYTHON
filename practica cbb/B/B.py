
def es_ordenable(a,b,r):
    for valores in (r):
        subA = a[valores[0]-1 : valores[1]]
        subB = b[valores[0]-1 : valores[1]]

        if sorted(subA) == subA and sorted(subB) == subB :
            print("YES")
        else:
            print("NO")


logitud = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

consultas = int(input(""))
rangos = [list(map(int,input().split())) for _ in range(consultas)]

es_ordenable(A,B,rangos)



