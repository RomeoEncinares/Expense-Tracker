from django import forms
from .models import transaction
from django.contrib.auth.forms import UserCreationForm

class transactionForm(forms.ModelForm):
    TRANSACTION_CHOICES = (('Income', 'Income'), ('Expense', 'Expense'))
    transactionType = forms.ChoiceField(widget=forms.RadioSelect(attrs={'id':'transactionType', 'style':'list-style:none'}), choices=TRANSACTION_CHOICES)
    CATEGORY_CHOICES = (
        ('Food & Drinks', 'Food & Drinks'),
        ('Shopping', 'Shopping'),
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

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}))

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)