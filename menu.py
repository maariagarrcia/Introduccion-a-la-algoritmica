import helpers
from colorama import Fore

def aceptarOpcionMenu():
    opcion = -1
    salir = False

    while (not salir):
        inputUsuario = input(Fore.GREEN + '· Dime, ¿que opción deseas? ' + Fore.WHITE)

        if (inputUsuario == 'F' or inputUsuario == 'f'): 
            # Finalizar
            opcion = -1
            salir = True
        elif (helpers.testInputInt(inputUsuario, 1, 6)): 
            # Jugar con un nivel entre el 1 y el 4
            opcion = int(inputUsuario)
            salir = True
        else:
            # Opción incorrecta
            print(Fore.RED + '* ATENCION:  Selecciona una opción valida ...' + Fore.WHITE)

    return opcion