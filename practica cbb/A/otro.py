MOD = 10**9 + 7
inverso_de_2 = pow(2, MOD - 2, MOD)

def main():
    cantidad_consultas = int(input("Número de consultas: "))
    resultados = []

    for _ in range(cantidad_consultas):
        x1, x2, y1, y2 = map(int, input("Ingresa x1 x2 y1 y2 separados por espacio: ").split())

        x_min = min(x1, x2)
        x_max = max(x1, x2)
        y_min = min(y1, y2)
        y_max = max(y1, y2)

        # Parte A: Celdas en la diagonal (x == y)
        inicio_diagonal = max(x_min, y_min)
        fin_diagonal = min(x_max, y_max)
        cantidad_diagonal = 0
        if inicio_diagonal <= fin_diagonal:
            cantidad_diagonal = (fin_diagonal - inicio_diagonal + 1) % MOD

        # Parte B: Celdas no diagonales (x < y)
        suma_no_diagonal = 0

        # Segmento 1: x en [x_min, min(x_max, y_min - 1)]
        inicio_seg1 = x_min
        fin_seg1 = min(x_max, y_min - 1)
        if inicio_seg1 <= fin_seg1:
            exp_a1 = y_max - fin_seg1
            exp_b1 = y_max - inicio_seg1
            if exp_a1 <= exp_b1:
                termino1 = (pow(3, exp_b1 + 1, MOD) - pow(3, exp_a1, MOD)) * inverso_de_2 % MOD
            else:
                termino1 = 0

            exp_a2 = y_min - fin_seg1 - 1
            exp_b2 = y_min - inicio_seg1 - 1
            if exp_a2 <= exp_b2:
                termino2 = (pow(3, exp_b2 + 1, MOD) - pow(3, exp_a2, MOD)) * inverso_de_2 % MOD
            else:
                termino2 = 0

            suma_segmento1 = (termino1 - termino2) % MOD
            suma_no_diagonal = (suma_no_diagonal + suma_segmento1) % MOD

        # Segmento 2: x en [max(x_min, y_min), min(x_max, y_max - 1)]
        inicio_seg2 = max(x_min, y_min)
        fin_seg2 = min(x_max, y_max - 1)
        if inicio_seg2 <= fin_seg2:
            exp_a3 = y_max - fin_seg2
            exp_b3 = y_max - inicio_seg2
            if exp_a3 <= exp_b3:
                termino3 = (pow(3, exp_b3 + 1, MOD) - pow(3, exp_a3, MOD)) * inverso_de_2 % MOD
            else:
                termino3 = 0

            cantidad_elementos = (fin_seg2 - inicio_seg2 + 1) % MOD
            suma_segmento2 = (termino3 - cantidad_elementos) % MOD
            suma_no_diagonal = (suma_no_diagonal + suma_segmento2) % MOD

        total = (cantidad_diagonal + suma_no_diagonal) % MOD
        total = (total + MOD) % MOD  # Asegura que sea positivo
        resultados.append(str(total))

    print("\nResultados:")
    print("\n".join(resultados))

main()
