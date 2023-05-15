from django.db import models

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

BOOKED      = "Booked"
AVAILABLE   = "Available"

room_availability =(
    (BOOKED, "BOOKED"),
    (AVAILABLE, "AVAILABLE")
)

class Rooms(models.Model):
    room_number     =models.CharField(max_length=50, null=False, blank=False)
    room_type       =models.CharField(max_length=50, choices=types, default=STANDARD, null=False, blank=False)
    availability    =models.CharField(max_length=50, choices=room_availability,default=AVAILABLE, null=False, blank=False)
    price           =models. FloatField(null=False, blank=False)   
    room_image      =models.FileField()       
    
