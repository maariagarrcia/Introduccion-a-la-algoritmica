#
# FUNCIONES  AUXILIARES
#

import os

# Limpiar la terminal.
# No funciona al ejecutar en ventana interactiva
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# Acepta un número entero
def inputInt(descripcion, min=None, max=None):
    while (True):
        inputUsuario = input('· '+ descripcion + '? ')

        if (inputUsuario == 'F' or inputUsuario == 'f'): 
            # Finalizar
            return None
        elif (testInputInt(inputUsuario, min, max)): 
            return int(inputUsuario)
        else:
            # Opción incorrecta
            print('  ATENCION: Valor NO válido ...')

# Valida si una cadena es número ente min y max
# DEVUELVE:
#   True -> Numero entre min y max
#   Falso -> No cumple los requisitos
## (Trozo de programa de validar el numero del 1er Cuatri)
def testInputInt(numero, min=None, max=None):
    try:
        # Convertir el input del usuario a tipo entero
        numero = int(numero)

    except:
        # El input no se ha podido convertir a tipo entero
        return False

    else:
        # Comprobar si esta en el rango especificado
        ok = True
        if (min!=None):
            ok = (min <= numero) 

        if (max!=None):
            ok =  ok and (numero <= max)
        
        return ok