c_confundible = ["l", "I", "O", "0", "B"]
def es_confundible(palabra):
    for caracteres in palabra:
        if caracteres in c_confundible:
            return "SI"
    return "NO"

cadena = input()
print(es_confundible(cadena))