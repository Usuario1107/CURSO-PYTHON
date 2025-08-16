persona = {
    "nombre": "Carlos",
    "edad": 28,
    "ciudad": "La Paz",
    "profesion": "Ingeniero",
    "casado": False,
    "hobbies": ["fútbol", "lectura", "viajar"],
    "contacto": {
        "email": "carlos@example.com",
        "telefono": "+591 76543210"
    }
}
#recorrer claves y valores de un dictionario
for clave,valor in persona.items():
    print(f"{clave} : {valor}")

# terminos de break y continue
"""  if clave == "ciudad":
        break # rompe el bucle
        #continue # salta la iteracion
"""
