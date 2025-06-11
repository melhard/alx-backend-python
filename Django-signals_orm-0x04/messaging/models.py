from django.db import models
from django.contrib.auth.models import User
from .managers import UnreadMessagesManager  # ⬅ استدعاء المدير المخصص

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    parent_message = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    objects = models.Manager()  # المدير الافتراضي
    unread = UnreadMessagesManager()  # المدير المخصص للرسائل غير المقروءة

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.content[:20]}"
