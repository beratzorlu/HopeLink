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


@login_required
def edit_blog(request, blog_id):
    """
    view to edit blog in the db
    """
    # checks if user has permition to add products
    if not request.user.groups.filter(name='site_admin').exists():
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'item was updated')
            return redirect(reverse('blog'))
        else:
            messages.error(
                request, 'item was not updated please check the from is valid'
            )
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """ Delete a blog from the store """
    if not request.user.groups.filter(name='site_admin').exists():
        messages.error(request, 'Sorry, only store admin can do that.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, f'{blog.title} deleted!')
    return redirect(reverse('blog'))
