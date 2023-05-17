from django.shortcuts import render
from Rooms.models import *
from Rooms.serializers import *
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
# Create your views here.

class RoomsListView(APIView):
    def get(self, request, format = None):
        queryset = Rooms.objects.all()[:20]
        rooms    = RoomSerializer(queryset, many=True)

        return Response(rooms.data)

class RoomObjectView(APIView):
    def get_room(self, slug):
        try:
            return Rooms.objects.get(slug=slug)
        except Rooms.DoesNotExist:
            return NotFound
        
    def get(self,request, slug, format=None):
        room_object = self.get_room(slug)
        room_serializer = RoomSerializer(room_object)
        return Response(room_serializer.data)
    
    def put(self, request, slug, format=None):
        room = self.get_room(slug)
        serializer = UpdateRoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request,slug, format=None):
        room = self.get_room(slug)
        room.delete()
        return Response(status=204)
    
class CreateRoomView(APIView):
    def post(self, request, format=None):
        serializer = CreateRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

