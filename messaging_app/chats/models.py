from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# 1. توسيع المستخدم الافتراضي
class User(AbstractUser):
    # أضف هنا أي خصائص إضافية إن وجدت لاحقًا (مثل صورة، حالة، إلخ)
    pass

# 2. نموذج المحادثة
class Conversation(models.Model):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id}"

# 3. نموذج الرسالة
class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.timestamp}"

