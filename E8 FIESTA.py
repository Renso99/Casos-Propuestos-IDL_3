# Inicio
print()
print('=== ASISTENCIA A UNA FIESTA ===')
print('===============================')
print()

# INICIALIZAR
Edad = 24
menor = 10000
hombres = 0 
mujeres = 0
cantidad_mujeres = 0
cantidad_hombres= 0

# VALIDACION --- PROCESO
print('SI DESEA SALIR. PRESIONE CERO')
while ( Edad != 0 ):
    Edad = int(input('INGRESE SU EDAD\n'))
    if(Edad>=18):
        if(Edad<menor):
            menor=Edad

        Sexo = int(input('INGRESE SU SEXO\n1. MASCULINO = 1\n0. FEMENINO = 0\n'))
        if(Sexo == 1):
            hombres = hombres + Edad
            cantidad_hombres = cantidad_hombres + 1
        else:
            mujeres = mujeres + Edad
            cantidad_mujeres = cantidad_mujeres + 1
    else:
        if(Edad!=0):
           
            print('NO SE PERMITE EL INGRESO DE MENORES DE EDAD')                      
# SALIDA
print()
print('EL PROMEDIO DE EDAD DE LAS MUJERES ' + str(mujeres / cantidad_mujeres))
print('EL PROMEDIO DE EDAD DE LOS HOMBRES ' + str(hombres / cantidad_hombres))
print('LAS PERSONAS QUE ASISTIENRON EN TOTAL A LA FIESTA ' + str(cantidad_mujeres + cantidad_hombres))
print('LA CANTIDAD DE MUJERES QUE ASISTIERON ' + str(cantidad_mujeres))
print('LA CANTIDAD DE HOMBRES QUE ASISTIERON ' + str(cantidad_hombres))
print('LA EDAD DE LA PERSONA MAS JOVEN QUE ASISTIO ' + str(menor))
print()
# FIN