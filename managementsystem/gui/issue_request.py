from django import forms
from .models import Order, Mail


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['category', 'order']

class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ['date_time']

        widgets = {
            'date_time':forms.TextInput(attrs={'type':'datetime-local'}),
        }