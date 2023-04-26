from django.contrib import admin
from django.urls import path, include
from .views import handler404, handler403, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('collection.urls')),
    path('accounts/', include('allauth.urls')),
    path('contact/', include('contact.urls')),
]

handler403 = "main.views.handler403"
handler404 = "main.views.handler404"
handler500 = "main.views.handler500"
