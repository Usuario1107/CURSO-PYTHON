sime_vertical = [
    "A" , "H" , "I" , "M" , "O" , "T" , "U" , "V" , "W" , "X" , "Y"]
sime_horizonal = ["B", "C", "D", "E", "H", "I", "K" , "O" , "X"]

def subcadena(x,y,cadena):
    salida = []
    for i,letra in enumerate(cadena):
        if i >= x and i<= y:
            salida.append(letra)
    return salida

def contar(subcadena):
    vertical = 0
    horizontal = 0
    for caracter in subcadena:
        if caracter in sime_vertical:
            vertical +=1
        if caracter in sime_horizonal:
            horizontal +=1
    return vertical,horizontal

mensaje = input()
tamaño = int(input())

indices = [list(map(int,input().split())) for _ in range(tamaño)]

for puntos in indices:
    x = puntos[0]
    y = puntos[1]
    subca = subcadena(x,y,mensaje)
    ver_max,hori_max = contar(subca)
    if ver_max == hori_max:
        print("Simetría igual.")
    elif ver_max > hori_max:
        print("Más simetría vertical.")
    elif hori_max > ver_max:
        print("Más simetría horizontal.")
