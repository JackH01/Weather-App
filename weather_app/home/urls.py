from django.urls import path
from . import views
from .forms import CityForm

urlpatterns = [
    path('home/', views.home, name='home'),
]
