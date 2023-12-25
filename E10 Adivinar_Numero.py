import random
# INICIO
print()
print('=== ADIVINAR NUMERO ===')
print('=======================')
print()

# INICIALIZAR
intentos = 0

# LECTURA
print('HOLA ¿CUAL ES TU NOMBRE?')
Nombre = input()
número = random.randint(1, 10)
print('BUENO, ' + Nombre + ', ESTOY PENSANDO UN NUMERO ENTRE 1 y 10.')

# VALIDACION Y PROCESO
while (intentos < 10):
    intentos = intentos + 1
    print('¿EN QUE NUMERO ESTAS PENSANDO?') 
    aproximado = input()
    aproximado = int(aproximado)
    
    if (aproximado < número):
        print('>>> EL NUMERO ES MAYOR AL QUE INSERTASTE <<<') 
        print()
    if (aproximado > número):
        print('>>> EL NUMERO ES MENOR AL QUE INSERTASTE <<<')
        print()
    if (aproximado == número):
        intentos = str(intentos)
        print()
        print('¡BUEN TRABAJO, ' + Nombre + '! ¡HAS ADIVINADO EN EL ' + intentos + ' INTENTO!')
        print()
if (aproximado != número):
        número = str(número)
# SALIDA
print()
print('EL NUMERO QUE ESTABA PENSANDO ERA EL ' + número)
print()
#FIN