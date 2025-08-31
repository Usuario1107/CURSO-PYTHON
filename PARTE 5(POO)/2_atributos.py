#ATRIBUTOS ES CASI LO MISMO QUE PROPIEDADES DE UN COSA
class ClaseCelular:
    def __init__(self,marca ,modelo): # __init() se ejecuta siempre cada vez que instanciamos   el self es para darle atributos dinamicos  que recibe como paraametro marca y celular 
        self.marca = marca  #self.marca es un atributo que la bamos igualar al parametro de marca y asi con todos 
        self.modelo = modelo 
        self.modelo_prueba = modelo # aqui esta definiendo otro atribo pero con el mismo modelo de parametro

celular1 = ClaseCelular("SAMSUNG","S25") # creamos pasamos una marca y modelo y qeu contiene marca modelo y modelo_pruebra que creamos con self
celular2 = ClaseCelular("IPHONE","18 PRO MAX")

print(celular2.marca)