from django.shortcuts import render
from .models import Message

def unread_messages_view(request):
    unread_messages = Message.unread.unread_for_user(request.user)  # ← مدير مخصص
    return render(request, 'unread_messages.html', {
        'messages': unread_messages
    })
