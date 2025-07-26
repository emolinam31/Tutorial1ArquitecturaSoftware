from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, ProductShowView, ProductIndexView, ProductCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='products'),  # Cambié 'index' por 'products'
    path('products/create/', ProductCreateView.as_view(), name='form'),  # Agregué la barra final
    path('products/<str:id>/', ProductShowView.as_view(), name='show'),  # Agregué la barra final
] 