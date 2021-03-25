from django.shortcuts import render

# Create your views here.

from django.shortcuts import render



def home(request):
    
    return render(request, 'blog/home.html', {'context':'Home Page'})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})