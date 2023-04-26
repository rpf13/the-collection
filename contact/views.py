from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Import my contact form class
from .forms import ContactForm


# Views for the contact form mail functionality
@method_decorator(login_required, name='dispatch')
class SendEmailView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('email_success')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        email_subject = f"Contact message from {name}"
        email_body = f"Sender: {name} <{email}>\n\n{message}"

        send_mail(
            email_subject, email_body, email, [
                settings.EMAIL_RECEIVE], fail_silently=False)

        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EmailSuccessView(TemplateView):
    template_name = 'contact/success.html'
