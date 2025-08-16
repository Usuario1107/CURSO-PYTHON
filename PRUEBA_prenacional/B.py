def parciales(parc_1, parc_2, parc_3):
    parciales = []
    parciales.append(parc_1)
    parciales.append(parc_2)
    parciales.append(parc_3)
    
    minimo = min(parciales)
    parciales.pop(parciales.index(minimo))
    return sum(parciales)/2

def promedio(notas):
    return (notas[0]*0.15) + (parciales(notas[1],notas[2],notas[3])*0.45) + (notas[4]*0.40)

t_pruebas = int(input())

pruebas = [list(map(int,input().split())) for _ in range(t_pruebas)]

for notas in pruebas:
    nota = promedio(notas)
    if nota > 50 :
        print("Si")
    else:
        print("No")
