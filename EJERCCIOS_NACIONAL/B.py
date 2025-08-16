sime_vertical = ["A", "H", "I", "M", "O", "T", "U", "V", "W", "X", "Y"]
sime_horizonal = ["B", "C", "D", "E", "H", "I", "K", "O", "X"]

mensaje = input().strip()
tamaño = int(input().strip())

n = len(mensaje)
vertical_arr = [0] * (n + 1)
horizontal_arr = [0] * (n + 1)

for i in range(n):
    letra = mensaje[i]
    vertical_arr[i + 1] = vertical_arr[i] + (1 if letra in sime_vertical else 0)
    horizontal_arr[i + 1] = horizontal_arr[i] + (1 if letra in sime_horizonal else 0)

for _ in range(tamaño):
    x, y = map(int, input().split())
    vertical = vertical_arr[y + 1] - vertical_arr[x]
    horizontal = horizontal_arr[y + 1] - horizontal_arr[x]
    
    if vertical > horizontal:
        print("Más simetría vertical.")
    elif horizontal > vertical:
        print("Más simetría horizontal.")
    else:
        print("Simetría igual.")