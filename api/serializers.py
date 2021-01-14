from rest_framework import serializers
from chat.models import ChatRoomMessage


class ChatMessageSerializer(serializers.ModelSerializer):
    message = serializers.CharField()
    sent_by = serializers.StringRelatedField()

    class Meta:
        model = ChatRoomMessage
        fields = ['message', 'sent_by']
