from django.urls import path
from .views import delete_user

urlpatterns = [
    # other paths...
    path('delete-account/', delete_user, name='delete_user'),
]
