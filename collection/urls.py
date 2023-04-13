# First we need to import our views from the current directory
from . import views
from django.urls import path
from .views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('', views.home, name='home'),
]
