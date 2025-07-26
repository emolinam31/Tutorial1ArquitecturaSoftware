from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.
class HomePageView(TemplateView):
    template_name = "pages/home.html"  
    
class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Your Name",
        })
        return context
    
class ContactPageView(TemplateView):
    template_name = "pages/contact.html" 
    
class Product:
    products = [
    {"id":"1", "name":"TV", "description":"Best TV", "price":800},
    {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":1200},
    {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price":150},
    {"id":"4", "name":"Glasses", "description":"Best Glasses", "price":200},
    ]
    
class ProductIndexView(View):
    template_name = 'products/index.html'
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)
    
class ProductShowView(View):
    template_name = 'products/show.html'
    def get(self, request, id):
        try:
            product = Product.products[int(id)-1]
        except(IndexError, ValueError):
            return HttpResponseRedirect('')
          
        viewData = {}
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] = product["name"] + " - Product information"
        viewData["product"] = product
        return render(request, self.template_name, viewData)