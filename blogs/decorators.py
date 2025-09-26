# accounts/decorators.py

from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def anonymous_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You are already logged in.")
            return redirect('home')  # change this if needed
        return view_func(request, *args, **kwargs)
    return _wrapped_view
