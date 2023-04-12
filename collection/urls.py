# First we need to import our views from the current directory
from . import views
from django.urls import path

app_name = 'collection'

urlpatterns = [
    # path('', views.home, name='home'),
]
