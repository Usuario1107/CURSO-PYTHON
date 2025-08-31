# metodos son como crear funiones hacen algo 
class ClaseCelular:
    def __init__(self,marca ,modelo): # tambien es metodo pero contructorcon
        self.marca = marca  
        self.modelo = modelo 
    
    def llamar(self): #creando un metodo para llamar
        print(f"Inicando llamada desde {self.modelo}") # con el self se referencia a los atributos

    def cortar(self):
        print(f"terminando llamada desde un {self.modelo}")

celular1 = ClaseCelular("SAMSUNG","S25") # creamos pasamos una marca y modelo y qeu contiene marca modelo y modelo_pruebra que creamos con self
celular2 = ClaseCelular("IPHONE","18 PRO MAX")

celular2.llamar() 
celular1.cortar() 