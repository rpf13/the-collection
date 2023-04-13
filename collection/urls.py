# First we need to import our views from the current directory
from . import views
from django.urls import path
from .views import HomeView, CollectionListView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('collections/', CollectionListView.as_view(), name='collection_list'),
    # path('', views.home, name='home'),
]
