from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Message, MessageHistory

# إشارة لتسجيل المحتوى القديم قبل التعديل
@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:  # يعني أن الرسالة موجودة بالفعل
        old_message = Message.objects.get(pk=instance.pk)
        if old_message.content != instance.content:
            MessageHistory.objects.create(
                message=instance,
                old_content=old_message.content
            )
            instance.edited = True  # تعيين أنها معدّلة
