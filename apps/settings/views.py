from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'settings/index.html')


def about(request): 
    return render(request, 'settings/about.html')


def contact(request): 
    return render(request, 'settings/contact.html')