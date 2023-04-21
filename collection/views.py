from django.shortcuts import render, redirect
from django.http import HttpResponse
# check if the next two imports can be combined
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Collection, Item


# Generic view to verify allauth - TO-BE-DELETED
# def home(request):
#     return HttpResponse("Welcome to my Django app")


# Home view to display main site - unauthorized
class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('collection_list'))
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


# View to update existing collection - authorized
@method_decorator(login_required, name='dispatch')
class CollectionUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                           UpdateView):
    model = Collection
    fields = ['collection_name', 'description', 'image']
    template_name = 'collection_update.html'
    success_url = reverse_lazy('collection_list')

    # Method to verify if updating user is the one who created it
    def test_func(self):
        collection = self.get_object()
        if self.request.user == collection.user:
            return True
        return False


# View to delete existing collection - authorized
@method_decorator(login_required, name='dispatch')
class CollectionDeleteView(LoginRequiredMixin, UserPassesTestMixin,
                           DeleteView):
    model = Collection
    template_name = 'collection_delete.html'
    success_url = reverse_lazy('collection_list')

    def test_func(self):
        collection = self.get_object()
        if self.request.user == collection.user:
            return True
        return False


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


# View to create a new item - authorized
@method_decorator(login_required, name='dispatch')
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['item_name', 'description', 'image', 'details']
    template_name = 'item_create.html'

    def form_valid(self, form):
        collection = get_object_or_404(Collection, pk=self.kwargs.get('pk'))
        form.instance.collection_id = collection
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'collection_detail', kwargs={'pk': self.kwargs.get('pk')})


# View to update existing item - authorized
@method_decorator(login_required, name='dispatch')
class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    fields = ['item_name', 'description', 'image', 'details']
    template_name = 'item_update.html'

    def get_success_url(self):
        return reverse_lazy(
            'item_detail', kwargs={'pk': self.object.pk})

    # Method to verify if updating user is the one who created it
    def test_func(self):
        item = self.get_object()
        if self.request.user == item.collection_id.user:
            return True
        return False


# View to delete existing item - authorized
@method_decorator(login_required, name='dispatch')
class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    template_name = 'item_delete.html'

    # Method to redirect after successful deletion
    def get_success_url(self):
        return reverse_lazy(
            'collection_detail', kwargs={'pk': self.object.collection.pk})

    # Method to verify if updating user is the one who created it
    def test_func(self):
        item = self.get_object()
        if self.request.user == item.collection.user:
            return True
        return False


# View to display the details of an item - authorized
@method_decorator(login_required, name='dispatch')
class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = 'item_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collection_id'] = self.object.collection_id
        return context
