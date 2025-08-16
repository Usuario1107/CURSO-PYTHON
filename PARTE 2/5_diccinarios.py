
dicccionarios = dict(   nombre = "will",
                        edad = 34)

# las listas no pueden ser clave pero si tuplas porque no son mutables
dicccionario_1 = {("nombre", 'apellido') : "will"}

# creando diccionaria con fromkeys() solo sirve cuando queremos dar un valor none a a todoas la claves a un solo valor
dicccionario_2 = dict.fromkeys(["nombre", "apellido"],"will")

print(dicccionario_2)