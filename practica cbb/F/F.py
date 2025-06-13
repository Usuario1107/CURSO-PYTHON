def es_triangular(num):
    resultado = (-1 + (1 + 8 * num) ** 0.5) / 2
    return "SI" if resultado.is_integer() else "NO"

cantidad = int(input(""))
numeros = input("")

lista_int = list(map(int, numeros.split()))

if cantidad == len(lista_int):
    for num in lista_int:
        print(es_triangular(num))
