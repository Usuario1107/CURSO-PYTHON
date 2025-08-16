def ganador(equi_1, equi_2):
    nombre_1, punto_1 = equi_1
    nombre_2, punto_2 = equi_2

    if punto_1 > punto_2:
        return (nombre_1, punto_1 - punto_2)
    elif punto_2 > punto_1:
        return (nombre_2, punto_2 - punto_1)
    else:
        if nombre_1 < nombre_2:
            return (nombre_1, 0)
        else:
            return (nombre_2, 0)

n = int(input())
equipos = []

for _ in range(n):
    nombre, puntos = input().split()
    equipos.append((nombre, int(puntos)))

while len(equipos) > 2:
    nueva_ronda = []
    for i in range(0, len(equipos), 2):
        nuevo = ganador(equipos[i], equipos[i+1])

        
        nueva_ronda.append(nuevo)
    equipos = nueva_ronda

campeon = ganador(equipos[0], equipos[1])[0]
subcampeon = equipos[0][0] if equipos[1][0] == campeon else equipos[1][0]


print(campeon)
print(subcampeon)





