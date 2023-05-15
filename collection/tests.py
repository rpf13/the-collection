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


# Class for tests with authenticated user, inheriting from mixin class
class CollectionTestCase(CollectionTestMixin, TestCase):
    """
    Load _setup_common mixin for generic data and setup additional
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
        response = self.client.get(reverse(
            'collection_detail', args=[self.collection.pk]
        ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'collection/collection_detail.html')

    """
    Test updating a collection, verify update has been executed
    and verify proper redirect to collection_list
    """
    def test_collection_update_view_authenticated(self):
        response = self.client.post(reverse(
            'collection_update', args=[self.collection.pk]), {
            'collection_name': 'Updated Collection',
            'description': 'Updated description'
        })
        self.assertEqual(response.status_code, 302)
        self.collection.refresh_from_db()
        self.assertEqual(self.collection.collection_name, 'Updated Collection')
        self.assertEqual(self.collection.description, 'Updated description')
        self.assertRedirects(response, reverse_lazy('collection_list'))

    """
    Test deleting a collection. GET request to the collection and verify 200
    Assert correct collection delete template
    POST request for deleting the collection and check response, which is
    302, redirected to collection list.
    Verify if collection still exists or not.
    """
    def test_collection_delete_view_authenticated(self):
        response = self.client.get(reverse(
            'collection_delete', args=[self.collection.pk]
        ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'collection/collection_delete.html')

        response = self.client.post(reverse(
            'collection_delete', args=[self.collection.pk]
        ))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('collection_list'))
        self.assertFalse(Collection.objects.filter(
            pk=self.collection.pk).exists()
        )

    """
    Test accessing collection details of pre-created test collection
    """
    def test_collection_detail_view_authenticated(self):
        response = self.client.get(reverse(
            'collection_detail', args=[self.collection.pk]
            ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'collection/collection_detail.html')

    """
    Test accessing the item details of pre-created test collection
    and test item
    """
    def test_item_detail_view_authenticated(self):
        response = self.client.get(reverse(
            'item_detail', args=[self.item.pk]
        ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'collection/item_detail.html')

    """
    Test creating a new item in the collection, which is built in the setUp
    check that the item exists after creating
    ckeck if correct 302 redirect to collection_detail happens after creation
    """
    def test_item_create_view_authenticated(self):
        response = self.client.post(reverse(
            'item_create', args=[self.collection.pk]), {
            'item_name': 'New Item',
            'description': 'New item description',
            'details': 'New item details'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Item.objects.filter(item_name='New Item').exists())
        self.assertRedirects(response, reverse_lazy(
            'collection_detail', kwargs={'pk': self.collection.pk}
        ))

    """
    Test updating an existing item, which has been created during setUp
    in the collection, which has been created during setUp.
    Verify the fields are all updated and that the correct 302 to
    item detail gets shown.
    """
    def test_item_update_view_authenticated(self):
        response = self.client.post(reverse(
            'item_update', args=[self.item.pk]), {
            'item_name': 'Updated Item',
            'description': 'Updated item description',
            'details': 'Updated item details'
        })
        self.assertEqual(response.status_code, 302)
        self.item.refresh_from_db()
        self.assertEqual(self.item.item_name, 'Updated Item')
        self.assertEqual(self.item.description, 'Updated item description')
        self.assertEqual(self.item.details, 'Updated item details')
        self.assertRedirects(response, reverse_lazy(
            'item_detail', kwargs={'pk': self.item.pk}
        ))

    """
    Test deleting an item. GET request to the item and verify 200
    Assert correct item delete template
    POST request for deleting the item and check response, which is
    302, redirected to collection detail.
    Verify if item still exists or not.
    """
    def test_item_delete_view_authenticated(self):
        response = self.client.get(reverse(
            'item_delete', args=[self.item.pk]
        ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'collection/item_delete.html')

        response = self.client.post(reverse(
            'item_delete', args=[self.item.pk]
        ))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy(
            'collection_detail', args=[self.collection.pk]
        ))
        self.assertFalse(Item.objects.filter(pk=self.item.pk).exists())
        self.assertRedirects(response, reverse_lazy(
                'collection_detail', kwargs={'pk': self.collection.pk}
        ))

    """
    Test about site with pre created user. Simple test to check 200 state
    """
    def test_about_view_authenticated(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'collection/about.html')


# Class for tests with unauthenticated user, inheriting from mixin class
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

    """
    Test if unauth. user accessing collection_create gets
    redirected to login site. Includes next parameter to state
    where user should be redirected after login.
    """
    def test_collection_create_view_unauthenticated(self):
        response = self.client.post(reverse('collection_create'), {
            'collection_name': 'New Collection',
            'description': 'New description'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/accounts/login/?next=' + reverse('collection_create')
        )

    """
    Test if unauth. user accessing collection_create gets
    redirected to login site. User gets logged in with setUp
    credentials and check if collection_create can be accessed
    after login.
    f-string is used to create expected url, combined with next
    parameter.
    """
    def test_collection_create_view_login_and_redirect(self):
        response = self.client.get(reverse('collection_create'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, f"{reverse('account_login')}?next={reverse('collection_create')}")  # noqa
        self.client.force_login(self.user)
        response = self.client.get(reverse('collection_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'collection/collection_create.html')
