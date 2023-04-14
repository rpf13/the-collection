from django.shortcuts import render, redirect
from django.http import HttpResponse
# check if the next two imports can be combined
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Collection


# Generic view to verify allauth - TO-BE-DELETED
# def home(request):
#     return HttpResponse("Welcome to my Django app")


# Home view to display main site - unauthorized
class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('home'))
        return super().get(request, *args, **kwargs)


# View to display collections list of authorized user
@method_decorator(login_required, name='dispatch')
class CollectionListView(LoginRequiredMixin, ListView):
    model = Collection
    template_name = 'collection_list.html'
    context_object_name = 'collections'
    paginate_by = 6

    def get_queryset(self):
        return Collection.objects.filter(
            user=self.request.user
            ).order_by('-created_on')


# View to create a new collection - authorized
@method_decorator(login_required, name='dispatch')
class CollectionCreateView(LoginRequiredMixin, CreateView):
    model = Collection
    fields = ['collection_name', 'description', 'image']
    template_name = 'collection_create.html'
    success_url = reverse_lazy('collection_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# View to display the items of a collection - authorized
# queryset method ensures to display only items of that
# particular user
@method_decorator(login_required, name='dispatch')
class CollectionDetailView(LoginRequiredMixin, DetailView):
    model = Collection
    template_name = 'collection_detail.html'
    context_object_name = 'collection'

    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = self.object.item_set.all()
        context['items'] = items
        return context
