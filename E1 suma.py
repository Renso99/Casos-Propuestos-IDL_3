# INICIO
print()
print('=== SUMA DE NUMEROS NATURALES ===')
print('=================================')
print()

# LECTURA
N=int(input('INGRESE LA CANTIDAD DE NUMEROS >>> '))

# PROCESO
resultado = 0

for i in range(1, N + 1):
    resultado = resultado + i

# SALIDA 
print()
print('LA SUMATORIA DE NUMEROS DESDE 1 HASTA ' + str(N) + " es: " + str(resultado))
print()
# FIN