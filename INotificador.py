#Brayan Alexis Bermudez Morales
# 1. Creamos la abstracción (Interfaz)
# - INotificador
from abc import ABC, abstractmethod


class INotificador(ABC):
    @abstractmethod
    def enviar(self, mensaje: str):
        pass
# 2. Implementaciones concretas
# - NotificadorEmail
class NotificadorEmail(INotificador):
    def enviar(self, mensaje: str):
        print(f"Enviando Email: {mensaje}")
# - NotificadorSMS
class NotificadorSMS(INotificador):
    def enviar(self, mensaje: str):
        print(f"Enviando SMS: {mensaje}")
# 3. Nueva funcionalida
# - NotificadorWhatsApp
class NotificadorWhatsApp(INotificador):
    def enviar(self, mensaje: str):
        print(f"Enviando WhatsApp: {mensaje}")

#gestor que accede para enviar las notificaciones adecuadas
class GestorNotificaciones:
    def __init__(self, notificador: INotificador):
        self.notificador = notificador

    def notificar_usuario(self, mensaje: str):
        self.notificador.enviar(mensaje)


# Uso
gestor = GestorNotificaciones(NotificadorWhatsApp())
gestor.notificar_usuario("Hola, tu pedido ha sido enviado.")
# Resultado : Enviando WhatsApp: Hola, tu pedido ha sido enviado.