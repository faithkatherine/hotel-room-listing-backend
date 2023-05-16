from Rooms.models import *

class UploadLocation():
    def room_location(instance, filename, **kwargs):
        filepath = 'rooms/{room_number}/{filename}'.format(
            room_number = str(instance.room_number), filename = filename
        )

        return filepath
