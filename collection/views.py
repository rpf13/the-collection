from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Collection


# Generic view to verify allauth - TO-BE-DELETED
# def home(request):
#     return HttpResponse("Welcome to my Django app")


# Home view to display main site, unauthorised
class HomeView(TemplateView):
    template_name = 'home.html'


# View to display collections list of a user
class CollectionListView(LoginRequiredMixin, ListView):
    model = Collection
    template_name = 'collection_list.html'
    context_object_name = 'collections'
    paginate_by = 6

    def get_queryset(self):
        return Collection.objects.filter(
            user=self.request.user
            ).order_by('-created_on')
