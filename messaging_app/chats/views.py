from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    """
    ViewSet لإدارة المحادثات:
    - عرض قائمة المحادثات
    - إنشاء محادثة جديدة
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    @action(detail=True, methods=['post'])
    def add_message(self, request, pk=None):
        """
        Endpoint لإضافة رسالة جديدة إلى محادثة موجودة.
        """
        conversation = self.get_object()
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(conversation=conversation, sender=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet لإدارة الرسائل:
    - عرض قائمة الرسائل
    - إنشاء رسالة جديدة مستقلة (يمكن تعديلها حسب المطلوب)
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        # مثلاً، يتم تعيين المرسل تلقائياً بناءً على المستخدم الحالي
        serializer.save(sender=self.request.user)
