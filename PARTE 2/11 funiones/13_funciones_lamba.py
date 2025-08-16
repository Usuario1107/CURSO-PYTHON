# funcion lamabda
numero_por_dos  = lambda x: x*2 # funcion anonima

numeros = [1,2,3,4,5,6,7,8,9,10]

# funion filter()

def par(numero):
    return True if numero % 2 == 0 else False

numeros_pares = list(filter(par,numeros)) # filtra los numeros pares de la lista numeros envia uno por uno la lista numeros a la funcion par y devuelve una lista con los numeros pares

# con lambda
lambda_impares = list(filter(lambda x: x%2 != 0 , numeros)) # filtra los numeros pares de la lista numeros envia uno por uno la lista numeros a la funcion lambda y devuelve una lista con los numeros pares

print(numeros_pares)
print(lambda_impares)