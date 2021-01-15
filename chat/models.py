from django.db import models
import uuid
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class ChatRoom(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')
    blocked_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name='blocked_by', null=True, blank=True)

    def clean(self):
        a_to_b = ChatRoom.objects.filter(user1=self.user1, user2=self.user2).exclude(pk = self.id)
        b_to_a = ChatRoom.objects.filter(user1=self.user2, user2=self.user1).exclude(pk = self.id)
        if a_to_b.exists() or b_to_a.exists():
            raise ValidationError(_('combination of user1 and user2 already exists'))
        if self.blocked_by:
            if self.blocked_by == self.user1 or self.blocked_by == self.user2:
                pass
            else:
                raise ValidationError(_('invalid blocked by'))

    def __str__(self):
        return str(self.id)


class ChatRoomMessage(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, editable=False)
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now=True)
