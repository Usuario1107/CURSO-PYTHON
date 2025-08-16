def es_primo(num):
    if num <= 1:
        return False
    elif num == 2:
        return True 
    else:
        for i in range(2,num):
                if num % i == 0:
                    return False
        else:
            return True
cantidad = int(input("n:"))
numeros = []
i = 0
while(cantidad != len(numeros)):
    i+=1
    if es_primo(i):
        numeros.append(i)

print(numeros)