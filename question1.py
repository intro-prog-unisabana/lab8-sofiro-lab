"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""

# TODO: Implementar según README.md
import sys

if len(sys.argv) != 3:
    print("Error: Invalid input! Enter numeric values only.")
else:
    try:
        carga_total = float(sys.argv[1])
        numero_soportes = float(sys.argv[2])

        if numero_soportes == 0:
            print("Error: Cannot divide by zero! Supports must be greater than zero.")
        else:
            resultado = carga_total / numero_soportes
            print(f"Load per support point: {resultado:.2f} N")

    except ValueError:
        print("Error: Invalid input! Enter numeric values only.")