# INICIO
print()
print('=== PORCENTAJE DE NUMEROS ===')
print('=============================')
print()

# INICIALIZAR
Menores15 = 0
Mayores50 = 0
Entre25y50 = 0
NoCumple = 0

# LECTURA
N=int(input('INGRESE LA CANTIDAD DE DATOS A INGRESAR >>> '))
# VALIDACION --- PROCESO
for i in range (0,N):
    N = int( input(f'INGRESE EL DATO >>>  {i+1} <<< '))
if(N <= 15):
        Menores15 = Menores15 + 1
        PorcMenores = Menores15 / N
        
        
if(N >= 25 and N <= 50):
        Entre25y50 = Entre25y50 + 1
        PorcEntre = Entre25y50 / N
                
                  
if(N > 50):
        Mayores50 = Mayores50 + 1
        PorcMayores = Mayores50 / N
if(N > 16 < 24):
        NoCumple+=1
        PorcNoCumple = NoCumple / N
# SALIDA 
print()
print('NUMEROS MENORES A 15 >>> ', PorcMenores )
print('NUMEROS ENTRE 25 Y 50 >>> ', PorcEntre)
print('NUMEROS MAYORES A 50 >>> ' , PorcMayores)
print(PorcNoCumple)

print()

# FIN