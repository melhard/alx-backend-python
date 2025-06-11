from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification

class MessagingTestCase(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username='sender', password='pass')
        self.receiver = User.objects.create_user(username='receiver', password='pass')

    def test_notification_created_on_new_message(self):
        msg = Message.objects.create(sender=self.sender, receiver=self.receiver, content='مرحبًا!')
        notifications = Notification.objects.filter(user=self.receiver, message=msg)
        self.assertEqual(notifications.count(), 1)  # تحقق من إنشاء إشعار واحد
