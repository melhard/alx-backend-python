from django.shortcuts import render
from .models import Message

def unread_messages_view(request):
    unread_messages = Message.objects.filter(
        receiver=request.user,
        read=False
    ).only('sender__username', 'content', 'timestamp').select_related('sender')

    return render(request, 'unread_messages.html', {
        'messages': unread_messages
    })
