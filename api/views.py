from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from chat.models import ChatRoomMessage, ChatRoom
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from . import serializers
from rest_framework.response import Response
from django.db.models import Q


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
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
        return ChatRoomMessage.objects.filter(room=chat_room_id)[::-1]
    pagination_class = StandardResultsSetPagination
    serializer_class = serializers.ChatMessageSerializer


class GetContacts(APIView):
    def get(self, request):
        return Response(data={'results': ChatRoom.objects.filter(Q(user1=request.user) | Q(user2=request.user)).values_list('id', 'user1__username', 'user2__username')})
