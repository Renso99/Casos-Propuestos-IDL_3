# INICIO
print()
print('=== PARES - IMPARES - POSITIVOS - NEGATIVOS ===')
print('===============================================')
print()

# INICIALIZAR
Pares = 0
Impares = 0
Positivos = 0
Negativos = 0

# VALIDACION ---- PROCESO
for i in range (1, 11):
    
    print ('NUMERO ' + repr (i))
    N = int (input ('INGRESE EL NUMERO >>> '))
    if (N % 2 == 0):
        Pares = Pares + 1
    else:
        Impares = Impares + 1
    if (N < 0):
            Negativos = Negativos + 1
    else:
            Positivos = Positivos + 1

# SALIDA
print() 
print ('CUANTOS SON NUMEROS PARES >>> ', repr (Pares))
print ('CUANTOS SON NUMEROS IMPARES >>> ', repr (Impares))
print ('CUANTOS SON NUMEROS POSITIVOS >>>',  repr (Positivos))
print ('CUANTOS SON NUMEROS NEGATIVOS >>> ', repr (Negativos))
print()
#FIN