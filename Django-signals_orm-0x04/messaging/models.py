from django.db import models
from django.contrib.auth.models import User

# نموذج الرسائل
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)  # المرسل
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)  # المستقبل
    content = models.TextField()  # محتوى الرسالة
    timestamp = models.DateTimeField(auto_now_add=True)  # وقت الإرسال

    def __str__(self):
        return f'رسالة من {self.sender} إلى {self.receiver}'

# نموذج الإشعارات
class Notification(models.Model):
    user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)  # المستخدم المستقبل للإشعار
    message = models.ForeignKey(Message, on_delete=models.CASCADE)  # الرسالة المرتبطة بالإشعار
    created_at = models.DateTimeField(auto_now_add=True)  # وقت إنشاء الإشعار
    is_read = models.BooleanField(default=False)  # حالة قراءة الإشعار

    def __str__(self):
        return f'إشعار للمستخدم {self.user} - رقم الرسالة: {self.message.id}'

