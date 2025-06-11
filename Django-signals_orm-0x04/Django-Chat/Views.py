from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout

@login_required
def delete_user(request):
    user = request.user
    logout(request)  # Log out user to avoid session issues after deletion
    user.delete()    # Delete user instance (triggers signals)
    return redirect('home')  # Redirect to homepage or login page, adjust as needed
