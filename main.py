"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file

try:
    if len(sys.argv) < 2:
        raise IndexError("Insufficient arguments provided!")

    file_path = sys.argv[1]

    if len(sys.argv) < 3:
        sys.exit()

    comando = sys.argv[2]

    tareas = read_todo_file(file_path)

    if comando == "view":
        print("Tasks:")
        for tarea in tareas:
            print(tarea)

    elif comando == "add":
        if len(sys.argv) < 4:
            raise IndexError('Task description required for "add".')

     