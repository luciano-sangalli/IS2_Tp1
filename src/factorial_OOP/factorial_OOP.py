#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número o rangos (ej. 4-8, -10, 40-)          *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Adaptado para IS2 - FCyT                                                *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    """Calcula el factorial de un número entero positivo."""
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

def procesar_y_calcular(entrada):
    """
    Analiza la entrada (número o rango) y calcula los factoriales correspondientes.
    Soporta formatos: 'n', 'n-m', '-m' (1 a m) y 'n-' (n a 60).
    """
    try:
        if "-" in entrada:
            partes = entrada.split("-")
            
            # Caso: "-10" -> desde 1 hasta 10
            if partes[0] == "":
                inicio = 1
                fin = int(partes[1])
            # Caso: "40-" -> desde 40 hasta 60
            elif partes[1] == "":
                inicio = int(partes[0])
                fin = 60
            # Caso: "4-8" -> desde 4 hasta 8
            else:
                inicio = int(partes[0])
                fin = int(partes[1])
        else:
            # Caso: número único "5"
            inicio = fin = int(entrada)

        # Validación de rango lógico
        if inicio > fin:
            print(f"Error: El inicio ({inicio}) no puede ser mayor al fin ({fin}).")
            return

        # Bucle de impresión de resultados
        for n in range(inicio, fin + 1):
            print(f"Factorial de {n}! es {factorial(n)}")

    except ValueError:
        print(f"Error: '{entrada}' no es un formato válido. Use números (5) o rangos (4-8).")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# --- Bloque Principal ---

if __name__ == "__main__":
    # 1. Verificar si se pasó un argumento por CLI
    if len(sys.argv) < 2:
        # Si no hay argumentos, se solicita por teclado (input)
        argumento = input("No se detectó argumento. Ingrese número o rango (ej. 4-8, -10, 40-): ")
    else:
        # Si hay argumento, se toma el primero
        argumento = sys.argv[1]

    # 2. Ejecutar la lógica de procesamiento
    if argumento:
        procesar_y_calcular(argumento)
    else:
        print("Debe informar un número o rango para continuar.")