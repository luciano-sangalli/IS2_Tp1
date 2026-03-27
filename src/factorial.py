#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num):
    "Calcula el factorial de un número entero positivo."
    if num < 0:
        return 0
    elif num == 0:
        return 1
    else:
        fact = 1
        while(num > 1):
            fact *= num
            num -= 1
        return fact

def procesar_entrada(entrada):
    "Analiza la cadena de entrada y determina los límites desde/hasta."
    desde = 1
    hasta = 60

    if "-" in entrada:
        partes = entrada.split("-")
        # Caso: "-hasta" (ej. -10)
        if partes[0] == "" and partes[1] != "":
            hasta = int(partes[1])
        # Caso: "desde-" (ej. 5-)
        elif partes[0] != "" and partes[1] == "":
            desde = int(partes[0])
        # Caso: "desde-hasta" (ej. 4-8)
        elif partes[0] != "" and partes[1] != "":
            desde = int(partes[0])
            hasta = int(partes[1])
    else:
        # Caso: número único
        desde = hasta = int(entrada)
    
    return desde, hasta

# 1. Verificar si se pasó argumento, si no, solicitarlo manualmente
if len(sys.argv) < 2:
    entrada_usuario = input("No se detectó argumento. Ingrese un número o rango (ej: 5, 4-8, -10, 5-): ")
else:
    entrada_usuario = sys.argv[1]

try:
    # 2 y 3. Procesar el rango y convertir a enteros
    inicio, fin = procesar_entrada(entrada_usuario)

    print(f"Calculando factoriales en el rango: {inicio} hasta {fin}")
    
    # 4. Calcular y mostrar resultados
    for i in range(inicio, fin + 1):
        print(f"Factorial {i}! es {factorial(i)}")

except ValueError:
    print("Error: Asegúrese de ingresar números válidos.")
