from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Class to create a new collection
class Collection(models.Model):
    collection_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collection_name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.collection_name


# Class to create a new item in a collection
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    collection_id = models.ForeignKey(Collection, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    details = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-added_on"]

    def __str__(self):
        return self.item_name
