#Declarar
import os
#Inicio
print()
print('=== PROMEDIO DE NOTAS APROBADAS Y DESAPROBADAS ===')
print('==================================================')
print()

# INICIALIZACION
ap = 0
des = 0
sumap = 0
sumde = 0 
cont = 0

# LECTURA
c=int(input("CANTIDAD DE NOTAS A INGRESAR \n"))

# VALIDACION --- PROCESO
while(c!=cont):
    nota=int(input(f"INGRESE LA NOTA {cont+1} >>> "))
    cont=cont+1
    if(nota>=11):
        sumap=sumap+nota
        ap=ap+1
        PromA=sumap/ap
    else:
        sumde=sumde+nota
        des=des+1
        PromD=sumde/des
 
# SALIDA DE DATOS
print()    
print('EL PROMEDIO DE APROBADOS ES >>> ', PromA )
print('EL PROMEDIO DE DESAPROBADOS ES >>> ', PromD)
print()
#FIN