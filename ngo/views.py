from django.shortcuts import render, redirect, reverse, get_object_or_404

# Create your views here.
def ngo(request):
    """
    view for blod page
    """
    ngo = ngo.objects.all()

    template = 'ngo/ngo.html'
    context = {
        'ngo': ngo,
    }

    return render(request, template, context)