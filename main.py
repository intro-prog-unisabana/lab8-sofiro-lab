"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file

try:
    if len(sys.argv) < 2:
        raise IndexError("Insufficient arguments provided!")

    if sys.argv[1] == "--help":
        print("""Usage: python main.py <file_path> <command> [arguments]...

Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.

Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")
        sys.exit()

    file_path = sys.argv[1]

    if len(sys.argv) == 2:
        sys.exit()

    tareas = read_todo_file(file_path)
    i = 2  

    while i < len(sys.argv):
        comando = sys.argv[i]

        if comando == "view":
            print("Tasks:")
            for tarea in tareas:
                print(tarea)
            i += 1

        elif comando == "add":
            if i + 1 >= len(sys.argv):
                raise IndexError('Task description required for "add".')

            nueva_tarea = sys.argv[i + 1]
            tareas.append(nueva_tarea)
            print(f'Task "{nueva_tarea}" added.')
            i += 2

        elif comando == "remove":
            if i + 1 >= len(sys.argv):
                raise IndexError('Task description required for "remove".')

            tarea_eliminar = sys.argv[i + 1]

            try:
                tareas.remove(tarea_eliminar)
                print(f'Task "{tarea_eliminar}" removed.')
            except ValueError:
                print(f'Task "{tarea_eliminar}" not found.')

            i += 2

        else:
            raise ValueError("Command not found!")

    write_todo_file(file_path, tareas)

except IndexError as e:
    print(e)

except ValueError as e:
    print(e)