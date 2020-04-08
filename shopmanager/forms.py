from django.forms import ModelForm
from django import forms
from .models import Shop,ItemQuerry

class NewShopForm(ModelForm):
    class Meta():
        model = Shop
        fields = ['name', 'shoptype', 'address','town','district','pin','phno']

class ItemQuerryForm(ModelForm):
    class Meta():
        model = ItemQuerry
        widgets = {
            'items' : forms.Textarea()
        }
        fields = ['items']

class AppoinmentForm(ModelForm):
    class Meta():
        model = ItemQuerry
        fields = ['appoinment','notes']