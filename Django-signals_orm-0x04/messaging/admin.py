from django.contrib import admin
from .models import Message, Notification

# تسجيل النماذج في لوحة التحكم
admin.site.register(Message)
admin.site.register(Notification)
