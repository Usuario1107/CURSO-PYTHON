class Persona:
    def __init__(self,nomb,eda,naci):
        self.nombre = nomb
        self.edad = eda
        self.nacimiento = naci
    def hablar(self):
        print("hablo")

class Empleado(Persona):
    def __init__(self,nomb,eda,naci,trabaj, salar ):
        super().__init__(nomb,eda,naci) # haciendo la herecia y añadiendo atributos

        self.trabajo = trabaj
        self.salario = salar

class Fejes(Persona):
    pass # pass  hereda todo de Persona

""" if 4> 5:
    pass """ #ejmplo de pass
# herencia jerarquica se basa es varias calses dependan de un sol clase padre ose crear mas hios

feje1 = Fejes("Alex",45,"Mexicano") # creamos un objeto que hereda atributos de la clase Persona
empleado1 = Empleado("adan",45,"ecuador","limpiado",2323)


print(empleado1.nombre)
empleado1.hablar()
feje1.hablar()