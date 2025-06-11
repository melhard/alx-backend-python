from django.db import models
from django.contrib.auth.models import User

class UnreadMessagesManager(models.Manager):
    def unread_for_user(self, user):
        return self.get_queryset().filter(receiver=user, read=False)\
            .select_related('sender')\
            .only('sender__username', 'content', 'timestamp')
