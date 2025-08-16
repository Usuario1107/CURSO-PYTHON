def ganador(equipo_1,equipo_2,p_1,p_2):
    if p_1 == p_2:
        return (equipo_1,0) if equipo_1 < equipo_2 else (equipo_2,0)
    elif p_1 > p_2:
        return equipo_1,(p_1 - p_2)
    elif p_2 > p_1:
        return equipo_2,(p_2 - p_1)
    

def win(equipos):
    res = []
    for i in range(0,int(len(equipos)),2):
        print(f"[{i}]= e1:{equipos[i][0]} p:{equipos[i][1]} e2:{equipos[i+1][0]} p:{equipos[i+1][1]}")
        g,p = ganador(equipos[i][0],equipos[i+1][0],equipos[i][1],equipos[i+1][1])
        res.append([g,p])
    return res

entrada = [["botafogo", 8],["psg", 5],["urawa", 9],["river", 10],["palmeiras", 6],["porto", 6],["monterrey", 9],["intermilan", 10]]

while(len(entrada) != 2):
    restantes = win(entrada)
    print(restantes)
    entrada = restantes

print("---------------------------")
print(f"{entrada[0][0]} {entrada[0][1]} s:{entrada[1][0]} {entrada[1][1]}")