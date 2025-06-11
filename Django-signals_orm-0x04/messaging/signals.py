from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Message, MessageHistory, Notification

@receiver(post_delete, sender=User)
def cleanup_user_related_data(sender, instance, **kwargs):
    # Delete messages sent or received by the user
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()

    # Delete notifications related to the user
    Notification.objects.filter(user=instance).delete()

    # Delete message history related to the user's messages
    MessageHistory.objects.filter(message__sender=instance).delete()
    MessageHistory.objects.filter(message__receiver=instance).delete()
