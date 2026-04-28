"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""

# TODO: Implementar según README.md
try:
    # Validar cantidad de argumentos
    if len(sys.argv) != 3:
        raise ValueError

    # Obtener argumentos
    carga_total = float(sys.argv[1])
    numero_soportes = float(sys.argv[2])

    # Validar división por cero
    if numero_soportes == 0:
        print("Error: Cannot divide by zero! Supports must be greater than zero.")
    else:
        carga_por_soporte = carga_total / numero_soportes
        print(f"Load per support point: {carga_por_soporte:.2f} N")

except ValueError:
    print("Error: Invalid input! Enter numeric values only.")