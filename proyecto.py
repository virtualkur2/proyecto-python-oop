#########################################################
# PROYECTO FINAL
#
# Autor:
#     Mauricio Contreras Canepa
# Fecha:
#     21/04/2021
# Profesor:
#     Enrique Hernandez
# Curso:
#     PROGRAMACIÓN EN LENGUAJE PYTHON [Curso Técnico]
##########################################################

import sys
from agenda import Agenda
from funciones import nombre_valido
from funciones import telefono_valido

# Instancia de la Agenda
agenda = Agenda('text', 'agenda.txt')


def menu():
    """Menú de opciones.

    Menú con las opciones del programa de agenda telefónica.

    Returns:
        Valor booleano que indica si se debe volver a mostrar el menú.
    """
    print('='*10, 'Menu Agenda', '='*10)
    print()
    print('1.- Obtener teléfono')
    print('2.- Insertar teléfono')
    print('3.- Eliminar teléfono')
    print('4.- Salir')
    print()
    op = input('Ingrese una opción: ').strip()

    if op == '1':
        # Obtenemos teléfono
        print()
        contacto = input('Nombre de contacto: ').strip()
        telefono = agenda.obten_telefono(agenda.fichero, contacto)
        if telefono:
            print('', '-'*(len(contacto) + len(telefono) + 4))
            print(f'| {contacto}: {telefono} |')
            print('', '-'*(len(contacto) + len(telefono) + 4))
    elif op == '2':
        # Insertamos teléfono
        print()
        while True:
            contacto = input('Nombre de contacto: ').strip()
            if nombre_valido(contacto):
                break
        while True:
            telefono = input('Número de teléfono: ').strip()
            if telefono_valido(telefono):
                break
        resultado = agenda.inserta_telefono(agenda.fichero, contacto, telefono)
        print()
        print(resultado)
        print()
    elif op == '3':
        # Eliminamos teléfono
        print()
        while True:
            contacto = input('Nombre de contacto: ').strip()
            if nombre_valido(contacto):
                break
        resultado = agenda.elimina_telefono(agenda.fichero, contacto)
        print()
        print(resultado)
        print()
    elif op == '4':
        # Salida del sistema
        print()
        print('Salida del sistema')
        print()
        return False
    else:
        # Opción no válida
        print()
        print('Opción no válida')
        print()
    return True


def main():
    """Ejecuta el programa.

    Función que realiza la ejecución del programa.

    Returns:
        Un valor entero indicando el código de salida.
    """
    muestra_menu = True
    try:
        while muestra_menu:
            muestra_menu = menu()
        return 0
    except KeyboardInterrupt:
        print()
        print('Se ha detectado la interrupción del programa.')
        print()
        return 1


if __name__ == '__main__':
    # Devuelve el resultado de la ejecución al método de salida del programa.
    sys.exit(main())
