conj_1 = {1,2,3,4,5}
conj_2 = {8,9}

# si es un subconbjunto entre los dos conjuntos
result = conj_1.issubset(conj_2) # false

result = conj_2.issubset(conj_1) #True
result = conj_2 <= conj_1 #True

result = conj_1.issuperset(conj_2) #True
result = conj_1 > conj_2 #True

# verificar si al uno en comun
comun_1 = conj_1.isdisjoint(conj_2) # true si no hay elementos en comun
comun_2 = conj_1.isdisjoint({1}) # false si hay elementos en comun
comun = bool(conj_1 & {6,7}) # true si no hay elementos en comun

print(comun_2)