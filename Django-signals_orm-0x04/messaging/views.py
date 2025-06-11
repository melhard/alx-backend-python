from django.views.decorators.cache import cache_page
from django.shortcuts import render
from .models import Message

@cache_page(60)  # تخزين لمدة 60 ثانية
def conversation_messages(request, conversation_id):
    messages = Message.objects.filter(conversation_id=conversation_id).order_by('timestamp')
    return render(request, 'messages/conversation.html', {'messages': messages})
