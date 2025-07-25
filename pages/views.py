from django.shortcuts import render
#from django.http import HttpResponse 
from django.views.generic import TemplateView

# Create your views here.
#def HomePageView(request):
    #return HttpResponse("Hello World Esteban Molina")
    
class homePageView(TemplateView):
    template_name = "home.html"