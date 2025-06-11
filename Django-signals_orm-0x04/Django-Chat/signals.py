from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Message, MessageHistory

# حفظ المحتوى السابق قبل التعديل
@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:  # الرسالة موجودة مسبقًا (ليست جديدة)
        old_message = Message.objects.get(pk=instance.pk)
        if old_message.content != instance.content:
            MessageHistory.objects.create(
                message=instance,
                old_content=old_message.content
            )
            instance.edited = True  # تأكيد أن الرسالة قد تم تعديلها
