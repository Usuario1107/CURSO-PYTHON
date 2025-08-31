# de clase atributo y metodos
# crear un clase Estudiante con atributos Nombre,Edad y Grado
# tenga metodo estudiar = "el estudiente {nombre} esta estudiando"
# crear objeto y usar el metodo
class Estudiante:
    def __init__(self,Nombre,Edad,Grado):
        self.nombre = Nombre
        self.edad   = Edad
        self.grado  = Grado
    
    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando")

nombre,edad,grado = input(":").split()
nombre = nombre.capitalize()
edad = int(edad)
grado = grado.capitalize()

estudiante1 = Estudiante(nombre,edad,grado)
estudiante1.estudiar()


