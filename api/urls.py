from Rooms import views as RoomViews
from django.urls import include, path

urlpatterns = [
    path('rooms/', RoomViews.RoomsListView.as_view()),
    path('rooms/<slug>/', RoomViews.RoomObjectView.as_view()),
    path('createRoom/', RoomViews.CreateRoomView.as_view()),
    path('updateRoom/<slug>/', RoomViews.RoomObjectView.as_view()),
    path('deleteRoom/<slug>/', RoomViews.RoomObjectView.as_view())
]