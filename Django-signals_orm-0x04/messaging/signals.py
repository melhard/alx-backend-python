from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message, Notification

# إنشاء إشعار تلقائي عند استلام رسالة جديدة
@receiver(post_save, sender=Message)
def create_notification_on_new_message(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)
