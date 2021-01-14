from django.urls import path
from .views import MessageRecordsView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('messages/<int:room_id>/', login_required(MessageRecordsView.as_view())),
]