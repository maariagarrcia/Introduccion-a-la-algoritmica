# Programa que pide por teclado que algoritmo desea calcular(mostrar por
# pantalla las posibles opciones) y que el usuario introduzca el número del 
# respectivo algoritmo que desee calcular(Comprobar que sea un 
# numero válido etc, lo de siempre).
# Cda vez que se introduzca un n´mero debe aparecer el título de lo que se
# está haciendo.
# Cada función tiene que tener mostrar titulo + su algoritmo + variables y
# que enseñe el resultado


### I M P O R T S
from colorama import *
import helpers
import menu

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
    # Leer datos
    numero_a = helpers.inputInt("Primer Valor (entero)")
    ponderacion_a = helpers.inputInt("Porcentaje ponderacion (0-100)")

    numero_b = helpers.inputInt("Segundo Valor (entero)")
    max_ponderacion_b = 100-ponderacion_a
    ponderacion_b = helpers.inputInt(
        "Porcentaje ponderacion (0-" + str(max_ponderacion_b)+")", 0, max_ponderacion_b)

    numero_c = helpers.inputInt("Tercer Valor (entero)")

    # Calcular y mostrar el resultado
    ponderacion_c = 100 - ponderacion_a - ponderacion_b
    media_ponderada = (numero_a*ponderacion_a/100 + numero_b *
                       ponderacion_b/100 + numero_c*ponderacion_c/100) 
    print()
    mostrar_resultado("Porcentaje ponderación (tercer valor)", ponderacion_c)
    mostrar_resultado("Media ponderada", media_ponderada)


# Ejercicio 10
def area_triangulo():
    mostrar_titulo("AREA TRIANGULO")

# Ejercicio 11
def salario_a_pagar():
    # Datos fijos
    # Se aplica entre 36 y 43 horas extra
    incremento_tarifa_horas_extra_tramo_1 = 1.25
    # Se aplica a partir de la 44 horas extra
    incremento_tarifa_horas_extra_tramo_2 = 1.50

    # Leer datos
    salario_bruto_mensual = helpers.inputInt(
        "Salario bruto mensual (entero positivo)", 1)
    horas_extra = helpers.inputInt("Horas extra mensuales (entero positivo)", 0)

    # Calculo tarifa normal horas extra
    salario_bruto_anual = salario_bruto_mensual * 12
    salario_bruto_semanal = salario_bruto_anual / 52
    tarifa_horas_normales = salario_bruto_semanal / 35

    # Calcular importe horas extra
    horas_extra_tramo_1 = 0
    horas_extra_tramo_2 = 0
    if (horas_extra > 8):
        horas_extra_tramo_2 = horas_extra - 8
        horas_extra_tramo_1 = 8
    elif (horas_extra > 0):
        horas_extra_tramo_1 = horas_extra

    importe_horas_extra_tramo_1 = horas_extra_tramo_1 * \
        tarifa_horas_normales * incremento_tarifa_horas_extra_tramo_1

    importe_horas_extra_tramo_2 = horas_extra_tramo_2 * \
        tarifa_horas_normales * incremento_tarifa_horas_extra_tramo_2

    importe_horas_extra_total = importe_horas_extra_tramo_1 + importe_horas_extra_tramo_2

    # Importe nómina
    importe_nomina = importe_horas_extra_total + salario_bruto_mensual

    # Mostrar resultados
    print()
    mostrar_resultado("Tarifa horas normales", tarifa_horas_normales)
    mostrar_resultado("Importe horas extra tramo 1 (" + str(horas_extra_tramo_1) + " horas a " +
                      str(tarifa_horas_normales *
                          incremento_tarifa_horas_extra_tramo_1)+")",
                      importe_horas_extra_tramo_1)
    mostrar_resultado("Importe horas extra tramo 2 (" + str(horas_extra_tramo_2) + " horas a " +
                      str(tarifa_horas_normales *
                          incremento_tarifa_horas_extra_tramo_2)+")",
                      importe_horas_extra_tramo_2)
    mostrar_resultado("Importe total horas extra", importe_horas_extra_total)
    mostrar_resultado("Importe TOTAL NOMINA", importe_nomina)


#
#
# I N I C I O    P R O G R A M A
#
#
helpers.clear()  # Limpia la terminal

while (True):
    opcion = menu.show()
    helpers.clear()

    if (opcion == 1):
        precio_con_impuestos()
    elif (opcion == 2):
        intereses_compuestos()
    elif (opcion == 3):
        media_aritmetica()
    elif (opcion == 4):
        media_ponderada()
    elif (opcion == 5):
        pass
    elif (opcion == 6):
        pass
    elif (opcion == 7):
        pass
    elif (opcion == 8):
        pass
    elif (opcion == -1):  # Salir
        print(Fore.GREEN + '> Nos vemos otro dia :-)')
        print(Fore.WHITE)
        break  # =============================>

    helpers.esperarIntro()