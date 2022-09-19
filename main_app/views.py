from datetime import date
from re import A
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import userProfile, balanceRecord, transaction
from .forms import transactionForm

def index(request):
    current_user = request.user
    print(current_user)
    return render(request, 'index.html')

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'register.html', context)

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print('Success')
            redirect('index')
            
    return render(request, 'login.html')

def homeView(request):
    form = transactionForm

    userObject = request.user
    userProfileModel = userProfile.objects.get(username=userObject)
    userBalance = userProfileModel.currentBalance

    userTransactionsModelSavings = transaction.objects.filter(username=userProfileModel, transactionType="Income")
    userTransactionsModelExpenses = transaction.objects.filter(username=userProfileModel, transactionType="Expense")

    userTransactionsModel = transaction.objects.filter(username=userProfileModel)
    recentUserTransactions = userTransactionsModel.order_by('-id')[:3]

    savingsAmount = 0
    expensesAmount = 0

    for i in userTransactionsModelSavings:
        savingsAmount += i.amount
    
    for j in userTransactionsModelExpenses:
        expensesAmount += j.amount
    
    balanceRecordModel = balanceRecord.objects.filter(username=userProfileModel)
    userBalanceRecord = balanceRecordModel.order_by('-id')[:5] 
    
    if request.method == 'POST':
        form = transactionForm(request.POST)
        transactionType = request.POST.get('transactionType')
        transactionCategory = request.POST.get('transactionCategory')
        amount = request.POST.get('amount')
        
        if transactionType == 'Income':
            userProfileModel.addTransaction('Income', float(amount))
            balanceRecord.objects.create(username=userProfileModel, balance=userBalance+float(amount))
        else:
            userProfileModel.addTransaction('Expense', float(amount))
            balanceRecord.objects.create(username=userProfileModel, balance=userBalance-float(amount))
        userProfileModel.save()

        transaction.objects.create(username=userProfileModel, transactionType=transactionType, transactionCategory=transactionCategory, amount=amount)
        
        return redirect('home')

    context = {
        'form': form,
        'recentUserTransactions': recentUserTransactions,
        'userBalanceRecord': userBalanceRecord,
        'userBalance': userBalance,
        'savingsAmount': savingsAmount,
        'expensesAmount': expensesAmount,
    }

    return render(request, 'home.html', context)

def transactionsView(request):

    userObject = request.user
    userProfileModel = userProfile.objects.get(username=userObject)
    userTransactionsModel = transaction.objects.filter(username=userProfileModel)

    context = {
        'userTransactionsModel': userTransactionsModel,
    }
    
    return render(request, 'transactions.html', context)       