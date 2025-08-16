# efercicio de fibonacci

def fibonacci(n):
    lista =[0]
    a,b = 0,1
    for i in range(n):
        print(f"a: {a}, b: {b}")
        if b > n: return lista
        lista.append(b)
        a,b = b, a+b
        """  # Usamos una variable temporal para actualizar los valores
        temp = a
        a = b
        b = temp + b """
    return lista

print(fibonacci(34))