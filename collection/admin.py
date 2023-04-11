from django.contrib import admin
from .models import Collection, Item

# Model registration
# might has to be changed to see all content of a user
# check admin site lessons for info
admin.site.register(Collection)
admin.site.register(Item)
