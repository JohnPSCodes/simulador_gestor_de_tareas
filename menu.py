'Imports'
from gestor import GestorTareas


# Inicializamos la clase Gestor de tareas
gt = GestorTareas()

# Funciones para manejar las selecciones del menu


def select_agregar():  # ✅
    intr_tarea = input('Describe con un nombre la tarea: ')
    print(f'✅ Tarea "{intr_tarea}" agregada correctamente!')
    gt.agregar(intr_tarea)


def select_listar():  # ✅
    gt.listar()


def select_completar():  # ✅
    intr_tarea = int(input('ID de la tarea completada: '))
    gt.completar(intr_tarea)
    print(f'La tarea {intr_tarea} marcada como completada ✅ ')


def select_guardar():
    intr_tarea = input('quieres guarda tu base de datos actual? (si/no): ')
    if intr_tarea == 'si':
        gt.guardar()
    elif intr_tarea == 'no':
        pass
    else:
        pass


def select_cargar():
    pass


def select_buscar():
    pass
