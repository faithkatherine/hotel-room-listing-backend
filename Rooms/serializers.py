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
    room_image = serializers.ImageField(required=False)
    class Meta:
        model = Rooms
        fields = ['room_number', 'room_type', 'availability', 'price', 'room_image', 'slug']
    
        def update(self, instance, validated_data):
            # Check if a new image file is provided
            if 'room_image' in validated_data:
                instance.room_image = validated_data['room_image']
            # Update other fields
            instance.room_number = validated_data['room_number']
            instance.room_type = validated_data['room_type']
            instance.availability = validated_data['availability']
            instance.price = validated_data['price']
            instance.slug = validated_data['slug']
            instance.save()
            return instance