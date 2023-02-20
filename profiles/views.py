from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile
from ngo.models import NGO
from blog.models import Blog
from django.db.models import Q


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


def search(request):
    query = request.GET.get('q')
    profile_results = []
    blog_results = []
    ngo_results = []

    if query:
        # Search Profile model
        profile_query = Q(user__username__icontains=query) | Q(
            phone_number__icontains=query)
        profile_results = Profile.objects.filter(profile_query)

        # Search Blog model
        blog_query = Q(title__icontains=query) | Q(body__icontains=query)
        blog_results = Blog.objects.filter(blog_query)

        # Search NGO model
        ngo_query = Q(name__icontains=query) | Q(
            description__icontains=query)
        ngo_results = NGO.objects.filter(ngo_query)

    context = {
        'profile_results': profile_results,
        'blog_results': blog_results,
        'ngo_results': ngo_results,
        'query': query,
        'from_search': True,
    }
    return render(request, 'profiles/profile.html', context)
