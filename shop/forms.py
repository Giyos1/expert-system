from django import forms
from shop.models import Product


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'slug', 'image', 'description', 'price', 'country')


class ProductCreateFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'slug', 'image', 'description', 'price']
