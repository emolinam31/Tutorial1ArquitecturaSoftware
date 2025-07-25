from django.shortcuts import render
from django.http import HttpResponse #New

# Create your views here.
def HomePageView(request):
    return HttpResponse("Hello World Esteban Molina")