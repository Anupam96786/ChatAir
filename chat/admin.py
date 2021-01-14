from django.contrib import admin
from .models import ChatRoom, ChatRoomMessage


admin.site.register(ChatRoom)
admin.site.register(ChatRoomMessage)
