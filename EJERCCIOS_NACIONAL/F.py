# bananitas fc
def repartir(habilidades,rango):
    iz = []
    der = []
    lon = len(habilidades)
    for i in range(lon-1):
        iz = habilidades[0:i+1]
        der = habilidades[i+1:lon]
        m = calcular_mejor(iz,rango[i][0])
        p = calcular_peor(der,rango[i][1])
        print(m-p)

def calcular_mejor(mejores,cantidad):
    mejores.sort(reverse = True)
    mejor = mejores[0:cantidad]
    return sum(mejor)

def calcular_peor(peores,cantidad):
    peores.sort()
    peor = peores[0:cantidad]
    return sum(peor)

hab = [3,4,1,5,6,2]
intervalos = [list(map(int,input("n:").split())) for _ in range(len(hab)-1)]

repartir(hab,intervalos)


