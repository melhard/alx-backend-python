from django.db import models
from django.contrib.auth.models import User

# نموذج الرسالة
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)  # ✅ لتتبع التعديلات

    def __str__(self):
        return f'رسالة من {self.sender} إلى {self.receiver}'

# نموذج سجل التعديلات
class MessageHistory(models.Model):
    message = models.ForeignKey(Message, related_name='history', on_delete=models.CASCADE)
    old_content = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)  # ✅ وقت التعديل

    def __str__(self):
        return f'تعديل لرسالة رقم {self.message.id} في {self.edited_at}'
