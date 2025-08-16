curso_rapido = 2.5
curso_promedio = 4
curso_lento = 7

el_curso = 1.5

difer_porcent_rapido = ((el_curso - curso_rapido)/curso_rapido )*100

difer_porcent_lento = ((el_curso - curso_lento)/curso_lento )*100

difer_porcent_promedio = ((el_curso - curso_promedio)/curso_promedio)*100


print(f"diferencia porcentaje curso actual y el masa rapido es: {difer_porcent_rapido} %")
print(f"diferencia porcentaje curso actual y el masa lento es: {difer_porcent_lento} %")
print(f"diferencia porcentaje curso actual y el masa promedio es: {difer_porcent_promedio} %")
print("-------")
crudo_prom_otros_curso = 5
crudo_prom_este_curso = 3.5

material_incervible_otros = ((crudo_prom_otros_curso - curso_promedio) / crudo_prom_otros_curso ) * 100

material_incervible_el_curso = ((crudo_prom_este_curso - el_curso) / crudo_prom_este_curso ) * 100

print(f"materia en porcentaje que no sirve de otros cursos es {material_incervible_otros} %")

print(f"materia en porcentaje que no sirve de el {material_incervible_el_curso} %")
print("-------------")

una_hora_del_curso = curso_promedio / el_curso

dies_horas_otros_cursos = ((el_curso ) / curso_promedio )*10

print(f"10 hora de este curso equivale a :{una_hora_del_curso * 10} hrs")
print(f"10 hora de otros cursos equivale a :{dies_horas_otros_cursos } hrs")

