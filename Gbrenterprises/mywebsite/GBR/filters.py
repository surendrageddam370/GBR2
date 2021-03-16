import django_filters
from .models import ItemList
from django.contrib.auth.models import User

class AddItemfilter(django_filters.FilterSet):
    class Meta:
        model = ItemList
         
        fields='__all__'
        exclude = ['item_name','item_quantity','item_gaze','item_dimensions','user']