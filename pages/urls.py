from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, ProductShowView, ProductIndexView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('pages/about/', AboutPageView.as_view(), name='about'),
    path("pages/contact/", ContactPageView.as_view(), name="contact"),
    path("products/", ProductIndexView.as_view(), name="products"),
    path("products/<int:id>", ProductShowView.as_view(), name="show"),
    
    
] 
