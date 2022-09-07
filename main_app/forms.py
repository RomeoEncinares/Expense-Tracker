from django import forms
from .models import transaction

class transactionForm(forms.ModelForm):
    TRANSACTION_CHOICES = (('Income', 'Income'), ('Expense', 'Expense'))
    transactionType = forms.ChoiceField(widget=forms.RadioSelect(attrs={'id':'transactionType', 'style':'list-style:none'}), choices=TRANSACTION_CHOICES)
    amount = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control', 'id':'amount'}))
    
    class Meta:
        model = transaction
        fields = ['transactionType', 'amount']