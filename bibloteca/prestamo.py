# prestamo.py
from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, copia, usuario, dias_prestamo: int = 7):
        self.copia = copia
        self.usuario = usuario
        self.fecha_inicio = datetime.now()
        self.fecha_vencimiento = self.fecha_inicio + timedelta(days=dias_prestamo)
        self.fecha_devolucion = None

    def ejecutar_prestamo(self) -> bool:
        if self.usuario.tiene_cupo() and self.copia.disponible:
            if self.copia.prestar():
                self.usuario.registrar_prestamo(self)
                return True
        return False

    def finalizar_devolucion(self) -> None:
        self.fecha_devolucion = datetime.now()
        self.copia.devolver()
        self.usuario.quitar_prestamo(self)