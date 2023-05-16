from django.apps import AppConfig


class RoomsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Rooms'

    def ready(self):
       import Rooms.signals.handlers 
