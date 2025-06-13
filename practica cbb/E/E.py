def main():
    salon_racso, cantidad_acciones = map(int, input("Ubicación y número de acciones: ").split())

    entregas_pendientes = dict()

    for _ in range(cantidad_acciones):
        entrada = input().strip()
        if entrada.startswith('E:'):
            entrada = entrada[2:].strip()

        partes = entrada.split()
        tipo = int(partes[0])

        if tipo == 1:
            destino = int(partes[1])
            entregas_pendientes[destino] = entregas_pendientes.get(destino, 0) + 1

        elif tipo == 2:
            destino = int(partes[1])
            if destino in entregas_pendientes:
                entregas_pendientes[destino] -= 1
                if entregas_pendientes[destino] == 0:
                    del entregas_pendientes[destino]

        elif tipo == 3:
            if not entregas_pendientes:
                print(0)
            else:
                minimo = min(entregas_pendientes)
                maximo = max(entregas_pendientes)
                distancia = max(abs(salon_racso - minimo), abs(salon_racso - maximo))
                print(distancia)

main()