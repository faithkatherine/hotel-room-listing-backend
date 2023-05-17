# Generated by Django 4.2.1 on 2023-05-17 09:23

from django.db import migrations, models

# Generated by Django 4.2.1 on 2023-05-17 09:26

from django.db import migrations

def update_availability(apps, schema_editor):
    Room = apps.get_model('Rooms', 'Rooms')
    for room in Room.objects.all():
        if room.availability == 'Available':
            room.availability = True
        else:
            room.availability = False
        room.save()




class Migration(migrations.Migration):

    dependencies = [
        ('Rooms', '0002_alter_rooms_options_alter_rooms_room_number'),
    ]

    operations = [
        migrations.RunPython(update_availability),
    ]