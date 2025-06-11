from django.urls import path
from .views import conversation_view

urlpatterns = [
    path('conversations/', conversation_view, name='conversation_view'),
]
