from django.db import models

class UnreadMessagesManager(models.Manager):
    def unread_for_user(self, user):
        return self.get_queryset().filter(
            receiver=user,
            read=False
        ).only('sender__username', 'content', 'timestamp').select_related('sender')
