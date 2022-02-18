### I M P O R T S
from email.mime import base
import helpers
import menu
from colorama import *
from cuenta import *

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
# PLANTEAMIENTO
# =============
# 1) Los triangulo tienen tres alturas, es decir que cada lado tiene una altura asociada.
#
# 2) Para calcular el area de un triangulo se necesita una combinación suficiente de datos
#    como la altura y la base (que no es el caso), los tres lados, dos lados y la altura, ...
#
# 3) Nosotro disponemos solo de un lado y su altura asociada por lo que si queremos calcular el area:
#       · Si el triangulo es escaleno => Los datos que tenemos son INSUFICIENTES
#       · es SUFICIENTE si es equilatero ya que cualquier lado actua como base.
#       · si es un triangulo isosceles hay dos caso:
#           1) La altura proporcionada es entre los lados congruentes -> DATOS INSUFICIENTE
#           2) La altura proporcionada es entre un lado respecto al lado incongruente -> SUFICIENTE,
#              ya dicha altura dividira el triangulo en dos semitriangulos simétricos....
#
# 4) Respecto al TRIANGULO RECTANGULO:
#       · Aplica lo anterior, es decir, solo se podra obtener el área si es isosceles (un angulo de
#           90º y dos de 45ª) y de nuevo hay dos casos:
#               1) El lado proporcionado es la hipotenusa. En este caso la altura coincidirá
#                  con uno de los catetos => DATOS SUFICIENTES 
#               2) El lado proporcionado no es la hipotenusa. En este caso será un un cateo 
#                  y la altura no aportaria información ya que será igual al cateto (y coincidente :-O )
#
def area_triangulo():
    mostrar_titulo("AREA TRIANGULO (Ver justificación en comentarios del coodigo)")
    print("1) El triangulo no puede ser escaleno")
    print("2) Si el triangulo es isosceles debe proporcionar uno de los lados incongruentes")
    print("   y la altura respecto al lado incongruente (que sera la base)")
    print()

    # Leer datos
    lado = helpers.inputReal("Lado (real positivo)", 0)
    altura = helpers.inputReal("Altura (real positivo)", 0)

    # Calcular la semibasebase y el área
    semibase = (lado**2 -altura**2) ** 0.5
    area = semibase * altura  
    es_equilatero = (2*semibase == altura)

    # Mostrar resultados
    mostrar_resultado("El triangulo es equilatero?", es_equilatero)
    mostrar_resultado("Base", semibase*2)
    mostrar_resultado("Área triangulo", area)

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

# Ejercicio 12
def cuenta_bancaria():   
    mostrar_titulo("GESTION CUENTAS BANCARIAS (Orientado a objetos)")

    # Crear una cuenta
    print("DATOS PARA CREAR LA CUENTA")
    titular = input("· Titular de la cuenta "+Fore.YELLOW)
    saldo_inicial = helpers.inputInt(Fore.WHITE+"Capital (entero)", 0)
    descubierto_permitido = helpers.inputInt("Descubierto permitido", 0)
    mi_cuenta = Cuenta(titular, saldo_inicial, descubierto_permitido)

    print("\n DATOS DE LA CUENTA")
    mostrar_resultado("Titular de la cuenta", mi_cuenta.titular)
    mostrar_resultado("Saldo", mi_cuenta.saldo)
    mostrar_resultado("Descubierto permitido", mi_cuenta.descubierto_permitido)
    print()

    # Operar con la cuenta
    print("OPERACIONES CON LA CUENTA")
    cantidad_a_ingresar = helpers.inputInt("Cantidad a ingresar", 0)
    mi_cuenta.ingresar(cantidad_a_ingresar)
    mostrar_resultado("Saldo despues del ingreso", mi_cuenta.saldo)


    cantidad_a_retirar = helpers.inputInt("Cantidad a retirar", 0)
    if mi_cuenta.retirar(cantidad_a_retirar):
        mostrar_resultado("Saldo despues de la retirada", mi_cuenta.saldo)
    else:
        print(Fore.RED + "Operación no permitida" + Fore.WHITE)



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
        area_triangulo()
    elif (opcion == 6):
        salario_a_pagar()
    elif (opcion == 7):
        cuenta_bancaria()

    elif (opcion == -1):  # Salir
        print(Fore.GREEN + '> Nos vemos otro dia :-)')
        print(Fore.WHITE)
        break  # =============================>

    helpers.esperarIntro()
