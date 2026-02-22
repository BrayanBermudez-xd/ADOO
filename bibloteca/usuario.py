# usuario.py
from typing import List
from prestamo import Prestamo

class Usuario:
    def __init__(self, idUsuario: int, nombre: str, limite_prestamos: int):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.limite_prestamos = limite_prestamos
        self.prestamos_activos: List[Prestamo] = []

    def tiene_cupo(self) -> bool:
        return len(self.prestamos_activos) < self.limite_prestamos

    def registrar_prestamo(self, prestamo: Prestamo) -> None:
        self.prestamos_activos.append(prestamo)

    def quitar_prestamo(self, prestamo: Prestamo) -> None:
        if prestamo in self.prestamos_activos:
            self.prestamos_activos.remove(prestamo)