from django.urls import path
from . import views

urlpatterns = [
    path('', views.medlembrete, name='medlembrete'),  
    
]
