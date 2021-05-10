"""Módulo de Agenda.

Este módulo contiene la definición de la Clase Agenda que implementa la lógica
necesaria de una agenda telefónica básica de tipo texto.

  Ejemplo de uso:

  agenda = Agenda(tipo, fichero)
  resultado = agenda.inserta_telefono(fichero, persona, telefono)
  resultado = agenda.elimina_telefono(fichero, persona)
  telefono = agenda.obten_telefono(fichero, persona)
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

import os


class Agenda:
    """Clase que implementa una agenda telefónica básica.

    Esta clase implementa las funciones necesarias para obtener, insertar y
    eliminar un contacto de la lista de contactos.

    Attributes:
        tipo: String que indica el tipo de agenda, por defecto agenda de texto.
        fichero: String que indica la ruta al fichero que almacena la agenda.
    """

    def __init__(self, tipo='text', fichero='agenda.txt'):
        """Incializa la Clase Agenda con tipo y fichero."""
        self.tipo = tipo
        self.fichero = os.path.join(os.getcwd(), fichero)
        if not os.path.exists(self.fichero):
            print(f'Fichero {self.fichero} no existe, se creará uno nuevo.')
            creado = self._create_file()
            if creado:
                print('Fichero creado satisfactoriamente.')
            else:
                print('Ocurrió un error al crear el fichero.')

    def _create_file(self):
        """Crea un nuevo fichero de agenda.

        Se encarga de la creación de un fichero nuevo para almacenar los datos
        de la agenda telefónica

        Returns:
            Un valor booleano indicando si la creación fue satisfacoria o no.
        """
        try:
            with open(self.fichero, 'x') as f:
                print(f'Fichero creado en: {f.name}')
                return True
        except FileExistsError:
            return False

    def _get_info(self, fichero):
        """Obtiene la información del fichero.

        Se encarga de leer el ficher de texto para extraer la información del
        mismo y volcarla en memoria en un diccionario.

        Args:
            fichero: Ruta al fichero que contiene los datos de la agenda.

        Returns:
            info: Diccionario con la información del fichero de agenda.
        """
        info = {}
        try:
            with open(fichero, 'r') as f:
                for line in f:
                    # Elimina el carácter de fin de línea
                    line = line.rstrip('\n')
                    # Obtiene el valor del primer campo
                    nombre = line.split(',')[0]
                    # Obtiene el valor del segundo campo
                    telefono = line.split(',')[1]
                    info[nombre] = telefono
        except FileNotFoundError:
            print()
            print(f'No se encuentra fichero: {fichero}')
            print()
        finally:
            return info

    def _save_info(self, fichero, info):
        """Guarda la información en el fichero de texto.

        Almacena la información de la genda en el fichero de texto.

        Args:
            fichero: Ruta al fichero que contiene los datos de la agenda.
            info: Diccionario con la información del fichero de agenda.
        Returns:
            Un valor booleano que indica si el proceso se realizó con éxito.
        """
        # Guardamos la agenda en el fichero
        try:
            with open(fichero, 'w') as f:
                # Iteramos sobre los items del diccionario
                for contacto, telefono in info.items():
                    # Creamos la linea a guardar
                    line = ','.join([contacto, telefono])+'\n'
                    # escribimos los datos
                    f.write(line)
                return True
        except FileNotFoundError:
            print()
            print(f'No se encuentra fichero: {fichero}')
            print()
            return False
        except PermissionError:
            print()
            print('Error de escritura, compruebe que tiene privilegios.')
            print()
            return False

    def obten_telefono(self, fichero, persona):
        """Obtiene un teléfono de la agenda, dado un contacto.

        Busca un teléfono en la agenda de acuerdo al nombre de un contacto,
        devuelve el teléfono encontrado o None en caso contrario.

        Args:
            fichero: Ruta al fichero que contiene los datos de la agenda.
            persona: Nombre del contacto del cual se desea obtener el teléfono.

        Returns:
            telefono: Número de teléfono del contacto o None.
        """
        # Obtenemos la información de la agenda
        agenda = self._get_info(fichero)
        telefono = agenda.get(persona)
        if not telefono:
            print()
            print(f'** No existe registro para {persona}. **')
            print()
            return
        return telefono

    def inserta_telefono(self, fichero, persona, telefono):
        """Inserta un contacto en la agenda o modifica uno existente.

        Inserta un nuevo contacto en la agenda telefónica. Si el contacto ya
        existe, pregunta si se debe actualizar el mismo o no.

        Args:
            fichero: Ruta al fichero que contiene los datos de la agenda.
            persona: Nombre del contacto a almacenar.
            telefono: Número de teléfono del contacto.

        Returns:
            Devuelve una cadena con el mensaje del resultado de la operación.
        """
        # Obtenemos la información de la agenda
        agenda = self._get_info(fichero)
        # Verificamos si la persona ya es un contacto almacenado
        if persona in agenda:
            print()
            print(f'** Ya existe un registro para {persona}. **')
            print()
            # Preguntamos si se desea actualizar el contacto
            while True:
                actualizar = input(
                    'Desea actualizar el registro? (s/n) ').strip()
                if actualizar.lower() in ['s', 'n']:
                    break
                print('Opción no válida, verifique.')
            if actualizar.lower() == 'n':
                return '** Actualización de registro cancelada. **'
            agenda[persona] = telefono
            return '** Registro actualizado correctamente. **'
        agenda[persona] = telefono
        saved = self._save_info(fichero, agenda)
        if saved:
            return '** Nueva entrada creada en la agenda. **'
        return '** Error insertando el registro, intente nuevamente. **'

    def elimina_telefono(self, fichero, persona):
        """Elimina un teléfono de la agenda.

        Se encarga de eliminar un registro de la agenda telefónica, dado un
        contacto.

        Args:
            fichero: Ruta al fichero que contiene los datos de la agenda.
            persona: Nombre del contacto a eliminar.

        Returns:
            Devuelve una cadena con el mensaje del resultado de la operación.
        """
        agenda = self._get_info(fichero)
        if persona in agenda:
            print()
            print(f'Se procederá a eliminar el contacto de {persona}.')
            print()
            while True:
                eliminar = input('¿Desea continuar? (s/n): ').strip()
                if eliminar.lower() in ['s', 'n']:
                    break
                print('Opción no válida, verifique.')
            if eliminar.lower() == 'n':
                return 'Eliminación de registro cancelada.'
            del agenda[persona]
            saved = self._save_info(fichero, agenda)
            if saved:
                return '** Registro eliminado correctamente. **'
            return '** Error eliminando registro, intente nuevamente. **'
        return f'** No existe registro para {persona}. **'


if __name__ == '__main__':
    print('Ejecute: python proyecto.py')
