from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URLs del admin de Django
    path('', include('pages.urls')),   # Incluye todas las URLs de la app 'pages'
]