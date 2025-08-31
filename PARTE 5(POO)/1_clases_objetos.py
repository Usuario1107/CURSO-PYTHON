class ClaseCelular(): # crear clase
    marca = "Snasung" # atributos estaticos
    modelo = "S35 PRO"
    ram = "45"

celular1 = ClaseCelular() # creando un objeto de la clase ClaseCelular no permite obetner todo lod atributos de esa clase
celular2 = ClaseCelular() # objeto es cuando se instancia una clase

print(celular1.modelo)
print(celular2.modelo)