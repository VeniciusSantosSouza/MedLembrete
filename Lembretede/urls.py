from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('medlembrete.urls')),  # Incluir URLs do app 'medlembrete'
    path('admin/', admin.site.urls),  # URL do admin
]
