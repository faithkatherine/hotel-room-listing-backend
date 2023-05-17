from typing import Any
from django.db import models
from .functions.upload_location import UploadLocation

# Create your models here.

STANDARD    = "Standard"
DOUBLE      = "Double Room"
SUITE       = "Suite"
EXECUTIVE   = "Executive"
DELUXE      = "Deluxe"
VILLA       = "Villa"

types=(
    (STANDARD, "STANDARD"),
    (DOUBLE, "DOUBLE"),
    (SUITE, "SUITE"),
    (EXECUTIVE, "EXECUTIVE"),
    (DELUXE, "DELUXE"),
    (VILLA, "VILLA")
)


class Rooms(models.Model):
    room_number     =models.CharField(max_length=50, null=False, blank=False, unique=True)
    room_type       =models.CharField(max_length=50, choices=types, default=STANDARD, null=False, blank=False)
    availability    =models.BooleanField(default=True)
    price           =models.FloatField(null=False, blank=False)   
    room_image      =models.FileField(upload_to=UploadLocation.room_location) 
    slug            =models.SlugField(null=False, blank=True) 

    class Meta:
        verbose_name = "Room"
    
    def __str__(self):
        return str(self.room_number)
    
    
