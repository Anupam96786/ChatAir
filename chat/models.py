from django.db import models
import uuid
from django.contrib.auth.models import User


class ChatRoom(models.Model):
    """
    docstring
    """
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, related_name='user2')

    class Meta:
        unique_together = ('user1', 'user2',)

    def __str__(self):
        return str(self.id)


class ChatRoomMessage(models.Model):
    """
    docstring
    """
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, editable=False)
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
