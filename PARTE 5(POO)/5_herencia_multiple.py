# se basa en que un clase hijo depende de dops o mas clases
# Clase Persona
class Persona:
    def __init__(self, Nombre, Edad, Pais):
        self.nombre = Nombre
        self.edad = Edad
        self.pais = Pais

    def saludar(self):
        return (f"Hola, soy {self.nombre} de {self.pais}.")
# Clase Trabajo
class Trabajo:
    def __init__(self, Ocupacion, Salario, Empresa):
        self.ocupacion = Ocupacion
        self.salario = Salario
        self.empresa = Empresa

    def describir(self):
        return (f"Trabajo como {self.ocupacion} en {self.empresa}, gano {self.salario} al mes.")

class Empleado(Persona,Trabajo):
    def __init__(self, Nombre, Edad, Pais,Ocupacion, Salario, Empresa,Hobby):
        Persona.__init__(self,Nombre, Edad, Pais) # heredando 3 atributo de Persona
        Trabajo.__init__(self,Ocupacion, Salario, Empresa) # Heredando 3 atributos de Trabajo

        self.hobby = Hobby # añadienndo un atributo mas
    def info(self):# creando un metodo corto de informacion
        return (f"hola soy {self.nombre} tengo {self.edad} años me gusta {self.hobby}")
    
    def jugar_futbol(self):
        return (f"yo juego {self.hobby} a las 5:pm")
    def descipcion(self):
        return (f"{super().saludar()} ---- {super().describir()} --{self.jugar_futbol()}") # para acceder metodo de la clase se usa self. pero par acceder a emtodo de padres se usa supper(). esto es lo correcto

persona1 = Empleado("Alex",34,"Argentina","Albañil",1200,"GOOGLE","Futbol") # creando objeto heredando atributos de Persona Trabajo y creando hobby

print(persona1.describir()) # metodo de Trabajo
print(persona1.saludar())  # metodo de Persona
print(persona1.info()  )    # metodo de Empleado
print(persona1.descipcion()) # metodo de clase Empleado

herencia = issubclass(Empleado,Trabajo) # dos clases y las compara su hereda algo
instancia = isinstance(persona1,Persona) # ygual pero de instancias 

print(herencia)
print(instancia)