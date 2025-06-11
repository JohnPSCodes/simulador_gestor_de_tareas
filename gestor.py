import json
import os
from tarea import Tarea


class GestorTareas():
    def __init__(self, archivo='tareas.json'):
        self.archivo = archivo
        self.tareas = []
        self.cargar()

    def agregar(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)
        self.guardar()

    def listar(self):
        for t in self.tareas:
            estado = '✅' if t.completada else '❌'
            print(f"[{t.id}] {estado} {t.descripcion} ({t.fecha_creacion})")

    def completar(self, id_tarea):
        tarea = self._buscar(id_tarea)
        tarea.completar()
        self.guardar()

    def _buscar(self, id_tarea):
        for t in self.tareas:
            if t.id == id_tarea:
                return t
        raise ValueError('Tarea no encontrada')

    def guardar(self):
        try:
            with open(self.archivo, 'w', encoding='utf=8') as f:
                json.dump([t.to_dict() for t in self.tareas], f, indent=2)
        except IOError as e:
            print('Error guardando archivo: ', e)

    def cargar(self):
        if not os.path.exists(self.archivo):
            return
        try:
            with open(self.archivo, 'r', encoding='utf=8') as f:
                data = json.load(f)
                self.tareas = [Tarea.from_dict(d) for d in data]
                if self.tareas:
                    Tarea._id_counter = max(t.id for t in self.tareas) + 1

        except (IOError, ValueError) as e:
            print('Error cargando archivo: ', e)
