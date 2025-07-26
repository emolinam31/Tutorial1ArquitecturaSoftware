from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views import View
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render, redirect
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
    
class ProductForm(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=100,
        error_messages={
            'required': 'El nombre del producto es obligatorio.',
            'max_length': 'El nombre no puede tener más de 100 caracteres.'
        }
    )
    price = forms.FloatField(
        required=True,
        error_messages={
            'required': 'El precio es obligatorio.',
            'invalid': 'Por favor ingrese un precio válido.'
        }
    )
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            # Eliminar espacios extra y convertir a título
            name = name.strip()
            if len(name) < 2:
                raise forms.ValidationError('El nombre debe tener al menos 2 caracteres.')
            if not name.replace(' ', '').isalnum():
                raise forms.ValidationError('El nombre solo puede contener letras, números y espacios.')
        return name
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None:
            if price <= 0:
                raise forms.ValidationError('El precio debe ser mayor que cero.')
            if price > 999999.99:
                raise forms.ValidationError('El precio no puede ser mayor a $999,999.99.')
        return price

class ProductCreateView(View):
    template_name = 'products/create.html'
    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            # Obtener los datos del formulario
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            
            # Crear un nuevo ID basado en el número de productos existentes
            new_id = str(len(Product.products) + 1)
            
            # Crear el nuevo producto
            new_product = {
                "id": new_id,
                "name": name,
                "description": f"Descripción para {name}",
                "price": price
            }
            
            # Agregar el producto a la lista
            Product.products.append(new_product)
            
            viewData = {}
            viewData["title"] = "Producto Creado"
            viewData["product"] = new_product
            return render(request, 'products/success.html', viewData)
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)