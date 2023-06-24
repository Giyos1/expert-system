from django import forms
from .models import Order, OrderItem


class OrderCreateForm(forms.ModelForm):
    """ModelForm class is used to create forms from models."""

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

