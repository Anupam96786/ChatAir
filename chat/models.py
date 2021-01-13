from django.db import models
import uuid
from django.contrib.auth.models import User


class ChatRoom(models.Model):
    """
    docstring
    """
    roomId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, related_name='user2')

    class Meta:
        unique_together = ('user1', 'user2',)

    def __str__(self):
        return self.roomId

