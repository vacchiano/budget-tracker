from django import forms
from django.forms import ModelForm

from .models import Transaction

class DateInput(forms.DateInput):
    input_type = 'date'

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'type', 'amount', 'description', 'category']
        widgets = {
            'date': DateInput(),
        }