from . import views
from django.urls import path


urlpatterns = [
    path(
        '', views.SendEmailView.as_view(), name='send_email'
    ),
    path(
        'success/', views.EmailSuccessView.as_view(), name='email_success'
    ),
]
