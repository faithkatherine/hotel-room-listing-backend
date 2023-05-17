"""HotelRoomListing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from HotelRoomListing import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Fallback errors
handler400 = lambda request, exception=None: JsonResponse({
          "status": "error",
          "code": 400,
          "data": None,
          "message": "Bad request"
        })

handler403 =  lambda request, exception=None: JsonResponse({
          "status": "error",
          "code": 403,
          "data": None,
          "message": "Your are not authorized to access this resource"
        })

handler404 =  lambda request, exception=None: JsonResponse({
          "status": "error",
          "code": 404,
          "data": None,
          "message": "The resource was not found"
        })

handler500 =  lambda request, exception=None: JsonResponse({
          "status": "error",
          "code": 500,
          "data": None,
          "message": "Oops! Server experienced an error."
        })
