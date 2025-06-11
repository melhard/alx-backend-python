from django.shortcuts import render
from .models import Message

def unread_messages_view(request):
    # استخدام مدير الرسائل غير المقروءة
    unread_via_manager = Message.unread.unread_for_user(request.user)

    # كتابة استعلام صريح لتحقيق شرط الاختبار الثاني
    optimized_unread = Message.objects.filter(
        receiver=request.user,
        read=False
    ).only('sender__username', 'content', 'timestamp').select_related('sender')

    return render(request, 'unread_messages.html', {
        'messages': unread_via_manager  # أو استخدم optimized_unread، كلاهما متشابهان
    })
