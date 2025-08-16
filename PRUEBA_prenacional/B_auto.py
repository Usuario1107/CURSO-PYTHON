cantidad_casos = int(input())

for _ in range(cantidad_casos):
    nota_practica, parcial1, parcial2, parcial3, nota_final = map(int, input().split())

    mejores_parciales = sorted([parcial1, parcial2, parcial3], reverse=True)[:2]
    promedio_parciales = sum(mejores_parciales) / 2

    promedio_ponderado = (
        0.15 * nota_practica +
        0.45 * promedio_parciales +
        0.40 * nota_final
    )

    if promedio_ponderado > 50:
        print("Si")
    else:
        print("No")
