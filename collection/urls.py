# First we need to import our views from the current directory
from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path(
        'collections/', views.CollectionListView.as_view(),
        name='collection_list'
        ),
    path(
        'collections/create/', views.CollectionCreateView.as_view(),
        name='collection_create'
        ),
    path(
        'collection/<int:pk>/', views.CollectionDetailView.as_view(),
        name='collection_detail'
        ),
    path(
        'collection/<int:pk>/update/', views.CollectionUpdateView.as_view(),
        name='collection_update'
    ),
    path(
        'collection/<int:pk>', views.CollectionDeleteView.as_view(),
        name='collection_delete'
    ),
    path(
        'collection/<int:pk>/create_item/', views.ItemCreateView.as_view(),
        name='item_create'
    ),
    path(
        'items/<int:pk>/update/', views.ItemUpdateView.as_view(),
        name='item_update'
        ),
    path(
        'items/<int:pk>/delete/', views.ItemDeleteView.as_view(),
        name='item_delete'
        ),
    path(
        'items/<int:pk>/', views.ItemDetailView.as_view(),
        name='item_detail'
        ),
    path(
        'about/', views.AboutView.as_view(),
        name='about'
    ),
]
