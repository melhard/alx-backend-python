from django.urls import path
from .views import conversation_messages

urlpatterns = [
    path('conversations/<int:conversation_id>/', conversation_messages, name='conversation_messages'),
]

