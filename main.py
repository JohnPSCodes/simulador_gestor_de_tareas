from menu import *


# interfaz para realizar acciones, realizado en la consola


def menu_controlador():

    print('\n\t  ===== MENU =====')
    print('\t= GESTOR DE TAREAS =')
    print("="*40)
    print("   ¿Qué deseas hacer? Elige una opción:")
    print("="*40, '\n')
    print("="*40)
    print('1.Agregar')
    print('2.Listar')
    print('3.Completar')
    print('4.Guardar')  # Eliminar o convertirlo en hacer Backup
    print('5.Cargar')
    print('6.Buscar')
    print('7.Salir')
    print("="*40, '\n')
    # Ejecucion del selector principal
    selector_principal()


def selector_principal():
    """
    Funcion que manejara las selecciones usando las funciones de seleccion y a la vez manejara excepciones
    """
    # Entrada para la seleccion del usuario

    seleccion = int(input('Selecciona una opcion: '))

    if seleccion == 1:  # ✅
        select_agregar()
        menu_controlador()

    elif seleccion == 2:  # ✅
        select_listar()
        menu_controlador()

    elif seleccion == 3:  # ✅
        select_completar()
        menu_controlador()

    elif seleccion == 4:  # 👁️
        select_guardar()
        menu_controlador()

    elif seleccion == 5:
        select_cargar()
        menu_controlador()

    elif seleccion == 6:
        select_buscar()
        menu_controlador()

    elif seleccion == 7:
        exit()
    else:
        print('Error Desconocido...')
        menu_controlador()


menu_controlador()
