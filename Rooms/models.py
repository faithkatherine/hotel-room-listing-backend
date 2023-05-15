from django.db import models

# Create your models here.

class Rooms(models.Model):
    room_number     =models.CharField(max_length=50)
    
