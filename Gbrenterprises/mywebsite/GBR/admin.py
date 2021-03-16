from django.contrib import admin
from .models import ItemList,AddItem
# Register your models here.
admin.site.register(AddItem)
admin.site.register(ItemList)