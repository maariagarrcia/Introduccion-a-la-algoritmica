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
import helpers

### F U N C I O N E S
def mostrar_titulo(titulo):
    print(Fore.YELLOW + titulo)
    print(Fore.WHITE)

def mostrar_resultado(descripcion,resultado):
    print(Fore.WHITE + "> " + descripcion + Fore.YELLOW, resultado, Fore.WHITE)

# Ejercicio 8
def precio_con_impuestos():
    mostrar_titulo("PRECIO CON IMPUESTOS")
    # Leer datos
    base_imponible = helpers.inputInt("Base Imponible (entero)")
    porcentaje_iva = helpers.inputInt("Porcentaje IVA (0-100)", 0, 100)

    # Mostrar el resultado
    precio_con_impuestos = base_imponible * (1 + porcentaje_iva/100)
    print()
    mostrar_resultado("Precio con impuestos incluidos", precio_con_impuestos)



# Calculo del interés compuesto .... https://es.wikipedia.org/wiki/Inter%C3%A9s_compuesto
# Calculo de potencias en python ... https://www.w3schools.com/python/python_operators.asp
def intereses_compuestos():
    mostrar_titulo("INTERESES COMPUESTOS (tipo periodo MENSUAL)")

    # Leer datos
    capital_inicial = helpers.inputInt("Capital (entero)")
    meses = helpers.inputInt("Meses en depósito (entero)", 1, 12)
    porcentaje_interes_mensual = helpers.inputInt(
        "Porcentaje Intereses MENSUAL (0-100)", 0, 100)

    # Mostrar el resultado
    # Capital final = C0 x (1+Ti) ^t
    capital_final = capital_inicial * \
        (1 + porcentaje_interes_mensual/100) ** meses
    print()
    mostrar_resultado("Capital Final", capital_final)


# Ejercicio 9

def media_aritmetica():
    mostrar_titulo("MEDIA ARITMETICA (3 numeros")
    # Leer datos
    numero_a = helpers.inputInt("Primer Valor (entero)")
    numero_b = helpers.inputInt("Segundo Valor (entero)")
    numero_c = helpers.inputInt("Tercer Valor (entero)")

    # Mostrar el resultado
    media_aritmetica = (numero_a + numero_b + numero_c) / 3
    print()
    mostrar_resultado("Media aritmetica", media_aritmetica)

    
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




