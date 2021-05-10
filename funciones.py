"""Módulo de funciones utilitarias.

Este módulo contiene funciones utilitarias de validación de nombre y teléfono
para ser usado por el programa de agenda

  Ejemplo de uso:

  es_valido = nombre_valido(nombre)
  es_valido = telefono_valido(telefono)
"""

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


def nombre_valido(nombre):
    """Valida el nombre de un contacto.

    Validación de la cadena recibida para comprobar que cumple con los
    requerimientos básicos de tamaño y tipos de caracateres.

    Args:
        nombre: String que representa el nombre a validar

    Returns:
        Un valor booleano que indica si el nombre superó la validación o no
    """
    # Cadena con los caracteres permitidos para nombres
    permitidos = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ '

    # Validamos que se recibe un valor para nombre
    if not nombre:
        print('No puede estar vacío, verifique por favor')
        print()
        return False
    # Validamos que el nombre tenga al menos 2 caracteres
    if len(nombre) < 2:
        print('Debe tener al menos 2 caracteres, verifique por favor')
        print()
        return False
    # Validamos cada caracter para saber si está dentro de los permitidos
    for caracter in nombre:
        if caracter.upper() not in permitidos:
            print(f'Caracter `{caracter}` no permitido, verifique por favor.')
            print()
            return False
    return True


def telefono_valido(telefono):
    """Valida un número de teléfono.

    Validación de la cadena recibida para comprobar que cumple con los
    requerimientos básicos de tamaño, tipo de caracateres y formato.

    Args:
        telefono: String que representa el telefono a validar

    Returns:
        Un valor booleano que indica si el teléfono superó la validación o no
    """
    # Validamos que se recibe algún valor
    if not telefono:
        print('Telefono no puede estar vacío, verifique')
        return False
    # Validamos que el teléfono tenga los 9 caracteres (España)
    if len(telefono) != 9:
        print('El telefono debe tener 9 caracteres')
        return False
    # Validamos que el teléfono comience con 6, 7, 8 o 9
    if not telefono.startswith(('6', '7', '8', '9')):
        print('El telefono debe comenzar con 6, 7, 8 o 9')
        return False
    # Validamos que cada caracter sea numérico
    if not telefono.isdigit():
        print('Teléfono debe contener sólo dígitos')
        return False
    return True


if __name__ == '__main__':
    print('Ejecute: python proyecto.py')
