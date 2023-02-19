from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile


# Create your views here.
@login_required
def profile(request):
    """Renders the friends list page"""
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile
    }
    template_name = 'profiles/profile.html'
    return render(request, template_name, context)
