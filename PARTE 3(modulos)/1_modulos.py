import modulo_saludar
# los modulos actual como objetos que llamamos a los atributos
modulo_saludar.Saludar("Daniel")

import modulo_despedida as adios
# es as es para  nosotros darle nombre al modulo actua ygual que el primero sirve tner un nmbre mas entendible
adios.Despedida("Carlos")

from mod_funciones import Suma,Resta
# para obtener los atributos especificos solo lo necesario tambien se lo renombre con AS
Suma()
Resta()

# ver propiedades de un modulo
print(dir(adios))
n_mod = adios.__name__ # trae el nombre del modulo aunque lo cambiemos el nombre para nuetro pagian que estemos trabajndo
print(n_mod)

print(type(modulo_saludar))
