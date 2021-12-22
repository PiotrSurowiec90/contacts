import django_filters
from django import forms
from django_filters import CharFilter

from .models import *

class ContactFilter(django_filters.FilterSet):
    name = CharFilter(field_name = 'name', lookup_expr="icontains",label='', widget = forms.TextInput(attrs = {'class':'contact-search'}))
    class Meta:
        model = Contact
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'search-bar', 'placeholder':"Full Name"}),
        }