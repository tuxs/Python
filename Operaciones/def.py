from lib.operaciones import *

valor = int(raw_input('ingrese un valor'))
valor2 = int(raw_input('ingrese otro valor'))
operacion = raw_input('que operacion desea realizar : {s - r - d - m}')

if operacion.lower() == 's':
    print suma(valor,valor2)
elif operacion.lower() == 'r':
    print resta(valor,valor2)
elif operacion.lower() == 'd':
    print division(valor,valor2)
elif operacion.lower() == 'm':
    print multiplicacion(valor,valor2)
    
