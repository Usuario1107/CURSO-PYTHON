def tamaño_m(clave):
    vector = []
    i = 0
    for letra in clave:
        if letra == "+":
            i+=1
            vector.append(i)
        elif letra == "-":
            i-=1
            vector.append(i)
    return vector



cadena = input()
valor = tamaño_m(cadena)
maximo = max(valor)

pocision = valor.index(maximo)+1


print(pocision)