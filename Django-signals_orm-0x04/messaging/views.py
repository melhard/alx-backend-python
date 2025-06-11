from django.shortcuts import render
from .models import Message

def conversation_view(request):
    # استرجاع الرسائل الأساسية التي ليست ردودًا
    top_level_messages = Message.objects.filter(
        receiver=request.user,
        parent_message__isnull=True
    ).select_related('sender', 'receiver').prefetch_related('replies')

    # دالة لتكرار الرسائل والردود
    def get_message_thread(message):
        return {
            'message': message,
            'replies': [get_message_thread(reply) for reply in message.replies.all()]
        }

    threads = [get_message_thread(msg) for msg in top_level_messages]

    return render(request, 'conversation.html', {'threaded_conversations': threads})
