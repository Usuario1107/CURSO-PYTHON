def es_lago(cadena):
    if len(cadena) > 10:
        return cadena[0] + str(len(cadena)-2) + cadena[-1]
    else:
        return cadena
n = int(input())
palabras = [input() for _ in range(n)] 
for palabra in palabras:
    print(es_lago(palabra))