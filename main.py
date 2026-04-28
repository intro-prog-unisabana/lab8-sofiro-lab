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
        
        nueva_tarea = sys.argv[3]
        tareas.append(nueva_tarea)
        write_todo_file(file_path, tareas)
        print(f'Task "{nueva_tarea}" added.')

    elif comando == "remove":
        if len(sys.argv) < 4:
            raise IndexError('Task description required for "remove".')

        tarea_eliminar = sys.argv[3]

        try:
            tareas.remove(tarea_eliminar)
            write_todo_file(file_path, tareas)
            print(f'Task "{tarea_eliminar}" removed.')
        except ValueError:
            print(f'Task "{tarea_eliminar}" not found.')

    else:
        raise ValueError("Command not found!")
    
except IndexError as e:
    print(e)

except ValueError as e:
    print(e)