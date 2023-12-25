import random
# INICIO
print()
print('=== HALLAR EL MAXIMO Y MINIMO ===')
print('=================================')
print()

# INICIALIZAR
mayor = -1000
cad = " " 
menor = 1000
Arrays = []

# VALIDACION----PROCESO
for i in range(100):
    ale = random.randrange(500) + 1
    Arrays.append(ale)
    cad = cad + " " + (str(ale))

for j in range(100):
    if(Arrays[j]>mayor):
        mayor = Arrays[j]

for x in range(100):
    if(Arrays[x]<menor):
        menor = Arrays[x]


# SALIDA
print()
print('LA LISTA DE NUMERO ES >>> ', cad)
print('EL NUMERO MAYOR ES >>>' + str(mayor))
print('EL NUMERO MENOR ES >>>' + str(menor))
print()
# FIN