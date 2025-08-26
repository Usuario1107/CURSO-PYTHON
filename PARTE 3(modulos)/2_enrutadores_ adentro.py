import carpeta1.mod_numeros as m_num
# estamos accediendo al modulo dentro de la carpeta1 a todo los modulos de mod_numeros
m_num.Primos()

from carpeta1.carpeta2.mod_nombres import Nombre_hombres,Nombre_mujeres as mujeres
# acceder a propiaedades especificos del modulo mod_nombes y renombreando uno de ello con as
Nombre_hombres()
mujeres()

