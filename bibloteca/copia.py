# copia.py
class Copia:
    def __init__(self, id_copia: str, libro, ubicacion: str):
        self.id_copia = id_copia
        self.libro = libro
        self.ubicacion = ubicacion
        self.disponible: bool = False

    def get_estado(self) -> str:
        return "Disponible" if self.disponible else "No disponible"

    def prestar(self) -> bool:
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self) -> None:
        self.disponible = True