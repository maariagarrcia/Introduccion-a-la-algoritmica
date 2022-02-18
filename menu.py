import helpers
from colorama import Fore

def aceptarOpcionMenu():
    opcion = -1
    while (True):
        inputUsuario = input(Fore.GREEN + '· Dime, ¿que opción deseas? ' + Fore.WHITE)

        if (inputUsuario == 'F' or inputUsuario == 'f'): 
            # Finalizar
            return -1 # =========================================>
        elif (helpers.testInputInt(inputUsuario, 1, 7)): 
            # Seleccionada una opción corredta
            return int(inputUsuario) # ==========================>
        else:
            # Opción incorrecta
            print(Fore.RED + '* ATENCION:  Selecciona una opción valida ...' + Fore.WHITE)

def show():
    helpers.clear()
    print(Fore.GREEN + 'MENU')
    print('====')
    print('1 - Precio con impuestos')
    print('2 - Importe intereses generados')
    print('3 - Media aritmetica de tres números')
    print('4 - Media ponderada de tres números')
    print('5 - Area de un triángulo' )
    print('6 - Calcular importe nómina')
    print('7 - Gestión cuenta bancaria')
    print('F - Finalizar')
    print(Fore.WHITE)

    return aceptarOpcionMenu()