numeros = [ 2,3 ,4,44,1,89,]

num_maximo = max(numeros)
num_minimo = min(numeros)

decimales = round(3.8345)  # redondear hacia arriba o abajo
dos_decimales = round(3.456, 2) # redondear a dos decimales

result_boleano = bool() # convertir a booleano
result_all = all([True,89,78,3]) # devuelve True si todos los elementos son verdaderos

sumar = sum(numeros) # suma todos los elementos de la lista

print(sumar)
print(result_boleano)
print(result_all)

print(num_maximo)
print(num_minimo)
print(decimales)
print(dos_decimales)