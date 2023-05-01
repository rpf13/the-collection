from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .models import Item, Collection
from . import views


# Create a Mixin for common setup code, used by both classes
class CollectionTestMixin:
    """
    create instance variables for user/pass
    setup a testuser and create with this user
    a testcollection and testitem
    """
    def _setup_common(self):
        self.username = 'testuser'
        self.password = 'testpassword-123'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )
        self.collection = Collection.objects.create(
            user=self.user,
            collection_name='Test Collection',
            description='This is a test collection'
        )
        self.item = Item.objects.create(
            item_name='Test Item',
            collection_id=self.collection,
            description='This is a test item',
            details='Details about the test item'
        )


# Class for tests with authenticated user
class CollectionTestCase(CollectionTestMixin, TestCase):
    """
    Load mixin for generic data and setup additional
    parameters used for authenticated testcases
    """
    def setUp(self):
        self._setup_common()
        self.client = Client()
        self.client.login(username=self.username, password=self.password)

    """
    Test home view for authenticated user
    user gets redirected to collection_list
    """
    def test_home_view_authenticated(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('collection_list'))

    """
    Test accessing collection_list of pre-created test collection
    """
    def test_collection_list_view_authenticated(self):
        response = self.client.get(reverse('collection_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'collection/collection_list.html')

    """
    Test creating a new collection, check proper redirect,
    make sure the new collection can be found
    """
    def test_collection_create_view_authenticated(self):
        response = self.client.post(reverse('collection_create'), {
            'collection_name': 'New Collection',
            'description': 'New description'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('collection_list'))
        self.assertTrue(Collection.objects.filter(
            collection_name='New Collection').exists()
        )

    """
    Test accessing collection detail view, which displays items in
    the collection. Pre-Created testdata will be used.
    """
    def test_collection_detail_view_authenticated(self):
        response = self.client.get(reverse('collection_detail', args=[self.collection.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'collection/collection_detail.html')


# Class for tests with unauthenticated user, inheriting from parent class
class UnauthenticatedCollectionTestCase(CollectionTestMixin, TestCase):
    """
    Load mixin for generic data and setup additional
    parameters used for unauthenticated testcases
    Log out the user for unauthenticated test case
    """
    def setUp(self):
        self._setup_common()
        self.client = Client()

    """
    Test home view for unauthenticated user
    user gets directed to home
    """
    def test_home_view_unauthenticated(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
