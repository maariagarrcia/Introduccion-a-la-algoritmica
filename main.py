# Programa que pide por teclado que algoritmo desea calcular(mostrar por
# pantalla las posibles opciones) y que el usuario introduzca el número del 
# respectivo algoritmo que desee calcular(Comprobar que sea un 
# numero válido etc, lo de siempre).
# Cda vez que se introduzca un n´mero debe aparecer el título de lo que se
# está haciendo.
# Cada función tiene que tener mostrar titulo + su algoritmo + variables y
# que enseñe el resultado



### I M P O R T S
from colorama import Fore
### F U N C I O N E S
def mostrar_titulo(titulo):
    print(Fore.YELLOW + titulo)
    print(Fore.WHITE)

def mostrar_resultado(descripcion,resultado):
    print(Fore.WHITE + "> " + descripcion + Fore.YELLOW, resultado, Fore.WHITE)

#Ejercicio 8
def precio_con_impuestos():
    mostrar_titulo("PRECIO CON IMPUESTOS")

def intereses_compuestos():
    mostrar_titulo("INTERESES COMPUESTOS (tipo periodo MENSUAL)")

#Ejercicii 9

def media_aritmetica():
    mostrar_titulo("MEDIA ARITMETICA (3 numeros")

def media_ponderada():
    mostrar_titulo("MEDIA PONDERADA (3 numeros) ")


# Ejercicio 10

def area_triangulo():
    mostrar_titulo("AREA TRIANGULO")







#
#
# I N I C I O    P R O G R A M A
#
#


### V A R I A B L E S   G L O B A L E S




