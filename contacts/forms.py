from django import forms

from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','relationship', 'email', 'adress', 'phone',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'type', 'placeholder':"Full Name"}),
            'relationship': forms.TextInput(attrs={'class': 'type', 'placeholder':"Relationship"}),
            'email': forms.TextInput(attrs={'class': 'type', 'placeholder':"@email"}),
            'adress' : forms.TextInput(attrs={'class': 'type', 'placeholder':"Adress"}),
            'phone': forms.TextInput(attrs={'class': 'type', 'placeholder': 'Telephone Number'})
        }