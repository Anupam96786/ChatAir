from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('api/', include('api.urls')),
]
