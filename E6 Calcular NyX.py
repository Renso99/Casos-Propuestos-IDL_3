#Declarar
import math
# INICIO
print()
print('=== CALCULAR LA SUMA ===')
print('========================')
print()

# INICIALIZACION
sum=0.0

# LECTURA
n=int(input('INGRESE EL VALOR DE N: \n'));
x=int(input('INGRESE EL VALOR DE X:\n'));
# VALIDACION-----PROCESO
for i in range(1,n+1):
    
    impar=2*i-1
    sum=sum+pow(x,impar)/impar

# SALIDA 
print()
print('LA SUMA TOTAL ES >>> ',)
print(str(round (sum,2)))
print()

# FIN