from gestor import GestorTareas
from menu import *
'''
Importacion de la clase GestorTareas, para utilizar sus metodos de gestion definidos
'''

# interfaz para realizar acciones, realizado en la consola
print('\n\t  ===== MENU =====')
print('\t= GESTOR DE TAREAS =')
print("="*40)
print("   ¿Qué deseas hacer? Elige una opción:")
print("="*40, '\n')
print("="*40)
print('1.Agregar')
print('2.Listar')
print('3.Completar')
print('4.Guardar')
print('5.Cargar')
print('6.Buscar')
print("="*40, '\n')
# Entrada para la seleccion del usuario
seleccion = int(input('Selecciona una opcion: '))


def selector_principal():
    """
    Funcion que manejara las selecciones usando las funciones de seleccion y a la vez manejara excepciones
    """
    if seleccion == 1:
        select_agregar()

    elif seleccion == 2:
        select_listar()

    elif seleccion == 3:
        select_completar()

    elif seleccion == 4:
        select_guardar()

    elif seleccion == 5:
        select_cargar()

    elif seleccion == 6:
        select_buscar()


# Ejecucion del selector principal
selector_principal()
