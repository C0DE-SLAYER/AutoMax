import django_filters
from django import forms

from .models import Listing

class ListingFilter(django_filters.FilterSet):

    mileage = django_filters.CharFilter(widget=forms.TextInput(attrs={'placeholder': '0'}))

    class Meta:
        model = Listing
        fields = {'brand': {'exact'}, 'mileage': {'exact'}}
