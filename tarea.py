"""Modulo de tiempo para usarlo en los registros de las tareas"""
from datetime import datetime


class Tarea:
    """
    Representa una tarea con ID único, descripción, estado de finalización
    y fecha de creación.
    """
    # Variable de clase para asignar ID unicos a las tareas
    _id_counter = 1

    def __init__(self, descripcion):
        """Constructor de la clase tarea"""
        self.id = Tarea._id_counter
        Tarea._id_counter += 1
        self.descripcion = descripcion
        self.completada = False
        self.fecha_creacion = datetime.now()

    def completar(self):
        """Marca la tarea como completada"""
        self.completada = True

    def to_dict(self):
        """Convierte el objeto Tarea en un diccionario (útil para guardar en JSON)"""
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "completada": self.completada,
            "fecha_creacion": self.fecha_creacion.isoformat()
        }

    @staticmethod
    def from_dict(data):
        """Constructor alternativo: crea un objeto Tarea a partir de un diccionario
        (por ejemplo, leído desde un JSON)"""
        t = Tarea(data["descripcion"])
        t.id = data["id"]
        t.completada = data["completada"]
        t.fecha_creacion = datetime.fromisoformat(data["fecha_creacion"])
        return t
