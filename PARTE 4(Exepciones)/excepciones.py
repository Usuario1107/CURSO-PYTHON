def suma():
    while True:
        try: 
            a = input("a:")
            b= input("b:")
            suma = int(a) + int(b) # ejmplo cuando sumamos string
        except: # si hay error en try: entra aca
            print("(x) error intenta de nuevo")
        else:# si no hay  excepcion
            break # SI SE EJECUTA LA SUMA todo biuen y salir
        finally: # se ejecuta siempre no importa si lanza una excepcion o no 
            print("ejecuta siempre no se porque lo crearon los hpt")
    print(suma)

def division():
    while True:
        try: 
            a = input("a:")
            b= input("b:")
            division = int(a) / int(b) # ejmplo cuando sumamos string
        except Exception as e: # asignando variable al error
            print(f"(x) error : {type(e).__name__}") # ver el nombre de la expecion podemos ver todas las expeciones q hay
        else:# si no hay  excepcion
            break # SI SE EJECUTA LA SUMA todo biuen y salir
    
    print(division)

division()