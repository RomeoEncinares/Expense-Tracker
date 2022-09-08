from django import forms
from .models import transaction

class transactionForm(forms.ModelForm):
    TRANSACTION_CHOICES = (('Income', 'Income'), ('Expense', 'Expense'))
    transactionType = forms.ChoiceField(widget=forms.RadioSelect(attrs={'id':'transactionType', 'style':'list-style:none'}), choices=TRANSACTION_CHOICES)
    CATEGORY_CHOICES = (
        ('Food & Drinks', 'Food & Drinks'),
        ('Shoppin', 'Shopping'),
        ('Housing', 'Housing'),
        ('Transportation', 'Transportation'),
        ('Vehicle', 'Vehicle'),
        ('Life & Entertainment', 'Life & Entertainment'),
        ('PC, Communication', 'PC, Communication'),
        ('Financial Investment', 'Financial Investment'),
        ('Investment', 'Investment'),
        ('Income', 'Income'),
        ('Others', 'Others'),
    )
    transactionCategory = forms.ChoiceField(widget=forms.Select(attrs={'id':'transactionCategory', 'class':'form-select', 'aria-label':'Default select example'}), choices=CATEGORY_CHOICES)
    amount = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control', 'id':'amount'}))
    
    class Meta:
        model = transaction
        fields = ['transactionType', 'transactionCategory', 'amount']