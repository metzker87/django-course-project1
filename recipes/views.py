from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Juliano Metzker',
    })


def aboutus(request):
    return HttpResponse("Contact us - Page")


def contactus(request):
    return render(request, 'recipes/contactus.html')