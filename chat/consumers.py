import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import ChatRoom, ChatRoomMessage
from django.contrib.auth.models import User


@database_sync_to_async
def get_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return AnonymousUser()


@database_sync_to_async
def get_room_users(room_id):
    try:
        chatroom = ChatRoom.objects.get(id=room_id)
        return [chatroom.user1, chatroom.user2]
    except:
        return []


@database_sync_to_async
def save_room_message(room_id, message, sent_by):
    # try:
    chatroom = ChatRoom.objects.get(id=room_id)
    ChatRoomMessage.objects.create(room = chatroom, sent_by=sent_by, message=message)
    # except:
    #     pass


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        if self.scope['user'].is_anonymous:
            await self.close()
        else:
            users = await get_room_users(self.room_name)
            if self.scope['user'] in users:

                # Join room group
                await self.channel_layer.group_add(self.room_name, self.channel_name)

                await self.accept()
            else:
                await self.close()


    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_name, self.channel_name)


    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # saving the messages to the database
        await save_room_message(self.room_name, message, self.scope['user'])

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.scope['user'].username
            }
        )


    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            "username": event["username"]
        }))
