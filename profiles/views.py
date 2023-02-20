from django.shortcuts import render, redirect, reverse, get_object_or_404
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
    blogs = Blog.objects.all().order_by("-added_on")
    ngos = NGO.objects.all().order_by('?')[:5]
    context = {
        'profile': profile,
        'blogs': blogs,
        'ngos': ngos,
    }
    template_name = 'profiles/profile.html'
    return render(request, template_name, context)


@login_required
def ngo_detail_views(request, ngo_id):
    ngo = get_object_or_404(NGO, pk=ngo_id)
    profile = Profile.objects.get(user=request.user)
    ngos = NGO.objects.all().order_by('?')[:5]
    context = {
        'profile': profile,
        'ngos': ngos,
        'ngo': ngo,
    }
    template_name = 'profiles/detail_view.html'
    return render(request, template_name, context)


@login_required
def blog_detail_views(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    profile = Profile.objects.get(user=request.user)
    ngos = NGO.objects.all().order_by('?')[:5]
    context = {
        'profile': profile,
        'ngos': ngos,
        'blog': blog,
        'from_blog': True,
    }
    template_name = 'profiles/detail_view.html'
    return render(request, template_name, context)


def search(request):
    """Handles Search querries for NGO Blog and Profile classes"""
    blogs = Blog.objects.all().order_by("-added_on")
    ngos = NGO.objects.all().order_by('?')[:5]
    profile = None
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
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)

    context = {
        'profile_results': profile_results,
        'blog_results': blog_results,
        'ngo_results': ngo_results,
        'query': query,
        'from_search': True,
        'profile': profile,
        'blogs': blogs,
        'ngos': ngos,
    }
    return render(request, 'profiles/profile.html', context)
