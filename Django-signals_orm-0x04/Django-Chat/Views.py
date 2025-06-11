from django.shortcuts import render
from .models import Message

def conversation_view(request):
    current_user = request.user

    # استرجاع الرسائل الرئيسية (التي ليست ردودًا)
    top_messages = Message.objects.filter(
        receiver=current_user, parent_message__isnull=True
    ).select_related('sender', 'receiver').prefetch_related('replies')

    # دالة لإرجاع الردود بشكل متداخل (متفرع)
    def get_message_thread(message):
        return {
            'message': message,
            'replies': [get_message_thread(reply) for reply in message.replies.all()]
        }

    threaded_conversations = [get_message_thread(msg) for msg in top_messages]

    return render(request, 'conversation.html', {
        'threaded_conversations': threaded_conversations
    })
