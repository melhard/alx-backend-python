from django.db import models
from django.contrib.auth.models import User

# مدير ORM مخصص للرسائل غير المقروءة
class UnreadMessagesManager(models.Manager):
    def for_user(self, user):
        return self.get_queryset().filter(receiver=user, read=False).only('sender', 'content', 'timestamp')

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    read = models.BooleanField(default=False)  # ➕ حقل لتتبع القراءة
    parent_message = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    # المدير الافتراضي
    objects = models.Manager()
    # مدير مخصص للرسائل غير المقروءة
    unread = UnreadMessagesManager()

    def __str__(self):
        return f'{self.sender} -> {self.receiver}: {self.content[:20]}'
