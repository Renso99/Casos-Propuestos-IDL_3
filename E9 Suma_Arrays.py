#INICIO
print()
print('=== CALCULAR LA SUMA ===')
print('========================')
print()

# INICIALIZAR
Arrays = []
suma=0
i=0

#VALIDAR.PROCESO
for i in range(0, 101):
    if (i % 2 == 0):
        Arrays.append(i)
        
for i in range(0, 101):
    suma += Arrays[i]
    
# SALIDA
    print()
    print ('LA SUMA TOTAL ES >>> ',suma )
    print()
# FIN
