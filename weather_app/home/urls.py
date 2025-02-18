from django.urls import path
from django.shortcuts import redirect
from . import views
from .forms import CityForm

urlpatterns = [
    path('', lambda req: redirect('home/')),
    path('home/', views.home, name='home'),
]
