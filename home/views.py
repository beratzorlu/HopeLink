from django.shortcuts import render


# Create your views here.
def index(request):
    """ a veiw to return index page """

    return render(request, 'home/index.html')