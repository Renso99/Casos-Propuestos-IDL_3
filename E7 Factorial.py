# INICIO
print()
print('=== HALLAR EL FACTORIAL ===')
print('===========================')
print()

# LECTURA 
num=int(input('INGRESAR EL VALOR >>> '))

# INICIALIZAR
factorial=1

# VALIDACION-------Proceso
for i in range(2,num+1):
	factorial*=i
	
# SALIDA 
print()
print('EL RESULTADO ES %d' % factorial)
print()

# FIN