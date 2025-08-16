def es_valido(repisa):
    for i in range(0,len(repisa),2):
        if repisa[i] != repisa[i+1]:
            return False
    return True

n = int(input("n:"))
repisa_1 = list(map(int,input("pesas:").split()))
repisa_2 = list(map(int,input("pesas:").split()))

if es_valido(repisa_1) and es_valido(repisa_2):
    print("SI")
else:
    print("NO")