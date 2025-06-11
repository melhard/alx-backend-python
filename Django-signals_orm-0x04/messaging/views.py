from django.shortcuts import render
from .models import Message

def conversation_view(request):
    # استرجاع كل الرسائل التي أرسلها المستخدم ولم تكن ردًا
    messages = Message.objects.filter(
        sender=request.user,
        parent_message__isnull=True
    ).select_related('sender', 'receiver').prefetch_related('replies')

    # دالة لاسترجاع الردود بشكل متكرر
    def get_message_thread(message):
        return {
            'message': message,
            'replies': [get_message_thread(reply) for reply in message.replies.all()]
        }

    # تجميع المحادثات
    threaded_conversations = [get_message_thread(msg) for msg in messages]

    return render(request, 'conversation.html', {
        'threaded_conversations': threaded_conversations
    })
