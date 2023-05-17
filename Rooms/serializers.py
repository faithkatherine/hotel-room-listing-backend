from rest_framework import serializers
from Rooms.models import *

import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model   =Rooms
        fields = ['room_number', 'room_type', 'availability', 'price', 'room_image', 'slug']
        read_only_fields = ['slug']

class CreateRoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rooms
        fields = ['room_number', 'room_type', 'availability', 'price', 'room_image']
    
    def create(self, validated_data):
        room_image = validated_data.pop('room_image')
        room = Rooms.objects.create(**validated_data)
        room.room_image = room_image
        room.save()
        return room



class UpdateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ['room_number', 'room_type', 'availability', 'price', 'room_image', 'slug']