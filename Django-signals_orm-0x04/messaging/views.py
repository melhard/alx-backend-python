from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout

@login_required
def delete_user(request):
    user = request.user
    logout(request)  # Log out the user first
    user.delete()    # Delete the user, triggering signals
    return redirect('home')  # Redirect to homepage (change if needed)
