# First we need to import our views from the current directory
from . import views
from django.urls import path
from .views import (
    HomeView,
    CollectionListView,
    CollectionCreateView,
    CollectionDetailView,
    CollectionUpdateView,
    CollectionDeleteView,
    ItemCreateView,
    ItemUpdateView,
    ItemDeleteView,
    ItemDetailView,
    ForbiddenView,
    NotFoundView,
    ServerErrorView,
    AboutView,
)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('collections/', CollectionListView.as_view(), name='collection_list'),
    path(
        'collections/create/', CollectionCreateView.as_view(),
        name='collection_create'
        ),
    path(
        'collection/<int:pk>/', CollectionDetailView.as_view(),
        name='collection_detail'
        ),
    path(
        'collection/<int:pk>/update/', CollectionUpdateView.as_view(),
        name='collection_update'
    ),
    path(
        'collection/<int:pk>', CollectionDeleteView.as_view(),
        name='collection_delete'
    ),
    path(
        'collection/<int:pk>/create_item/', ItemCreateView.as_view(),
        name='item_create'
    ),
    path(
        'items/<int:pk>/update/', ItemUpdateView.as_view(),
        name='item_update'
        ),
    path(
        'items/<int:pk>/delete/', ItemDeleteView.as_view(),
        name='item_delete'
        ),
    path(
        'items/<int:pk>/', ItemDetailView.as_view(),
        name='item_detail'
        ),
    path(
        '403/', ForbiddenView.as_view(),
        name='403'
    ),
    path(
        '404/', NotFoundView.as_view(),
        name='404'
    ),
    path(
        '500/', ServerErrorView.as_view(),
        name='500'
    ),
    path(
        'about/', AboutView.as_view(),
        name='about'
    ),
]
