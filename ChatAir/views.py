from django.shortcuts import render
from chat.models import ChatRoomMessage, ChatRoom
from asgiref.sync import async_to_sync
from django.http.response import HttpResponse


def get_messages(room_name):
    return list(ChatRoomMessage.objects.filter(room=ChatRoom.objects.get(id=room_name)).values_list('message', 'sent_by__username'))


def get_room_users(room_id):
    try:
        chatroom = ChatRoom.objects.get(id=room_id)
        return [chatroom.user1, chatroom.user2]
    except:
        return []


def index(request):
    return render(request, 'index.html')


def room(request, room_name):
    return render(request, 'a.html', {'room_name': room_name})
