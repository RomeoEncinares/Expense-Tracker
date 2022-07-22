from django import forms
from .models import transaction

class transactionForm(forms.Form):
    TRANSACTION_CHOICES = (('S', 'Savings'), ('E', 'Expenses'))
    transactionType = forms.ChoiceField(widget=forms.RadioSelect, choices=TRANSACTION_CHOICES)
    amount = forms.FloatField()
    
    class Meta:
        model = transaction
        fields = ['transactionType', 'amount']