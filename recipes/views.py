from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Home page")


def aboutus(request):
    return HttpResponse("About us - Page")


def contactus(request):
    return HttpResponse("Contact us - Page")