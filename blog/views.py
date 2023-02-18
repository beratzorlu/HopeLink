from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Blog



def blog(request):
    """
    view for blod page
    """
    blog = Blog.objects.all()

    template = 'blog/blog.html'
    context = {
        'blog': blog,
    }

    return render(request, template, context)

def add_blog(request):
    """
    veiw to add a blog post
    """
    