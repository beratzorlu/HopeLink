from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages



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

@login_required
def add_blog(request):
    """
    view to add products to the db
    """
    # checks if user has permition to add products
    if not request.user.groups.filter(name='site_admin').exists():
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'blog Added')
            return redirect(reverse('blog',))
        else:
            messages.error(
                request,
                'The blog was not added. Please check the form is valid.'
            )
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)