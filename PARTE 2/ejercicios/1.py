# el profe no vino a clase y los alumnos se pusieron a hacer la lista 1 alunmo es el profe y otro otro el asistente pedir nombre y edad a los alumnos 

# 1. mostrar de mayor a menor los datos 
# 2. el mayor es el profesor y el menor el asistente mostrar los datos
def ordenar_alumnos(alumnos):
    for i in range(len(alumnos)):
        for j in range(i,len(alumnos) -1):
            if alumnos[i][1] < alumnos[j+1][1]:
                temp =  alumnos[i]
                alumnos[i] = alumnos[j+1]
                alumnos[j+1] = temp
            
    return alumnos

def mostar_datos(alumnos):
    print("lista de alumnos de mayor a menor")
    for alumno in alumnos:
        print(f"{alumno[0]} {alumno[1]}")
    print(f" el profesor es {alumnos[0][0]}")
    print(f" el asistente es {alumnos[-1][0]}")

n =  int(input("cantidad de alumnos: "))
alumnos = []

for i in range(1,n+1):
    alumno = list(input(f"ingrese el n y e del alumno {i}: ").split())
    alumno[1]= int(alumno[1])  # Convertir la edad a entero
    alumnos.append(alumno) # agregar a la lista

mostar_datos(ordenar_alumnos(alumnos))
