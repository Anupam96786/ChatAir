from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from chat.models import ChatRoomMessage
from rest_framework.generics import ListAPIView
from . import serializers
from rest_framework.response import Response


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    def get_paginated_response(self, data):
        return Response({
            'previous': self.get_previous_link(),
            'next': self.get_next_link(),
            'page_number': self.page.paginator.num_pages,
            'results': data,
        })


class MessageRecordsView(ListAPIView):
    def get_queryset(self):
        chat_room_id = self.kwargs['room_id']
        return ChatRoomMessage.objects.filter(room=chat_room_id)
    pagination_class = StandardResultsSetPagination
    serializer_class = serializers.ChatMessageSerializer
