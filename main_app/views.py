from re import A
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import userProfile, transaction
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

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print('Success')
            redirect('index')
            
    return render(request, 'login.html')

def homePage(request):
    form = transactionForm

    currentUserObject = request.user
    currentUserModel = userProfile.objects.get(username=currentUserObject)

    if request.method == 'POST':
        form = transactionForm(request.POST)
        transactionType = request.POST.get('transactionType')
        amount = request.POST.get('amount')
        
        if transactionType == 'S':
            currentUserModel.addTransaction('savings', float(amount))
        else:
            currentUserModel.addTransaction('expense', float(amount))
        currentUserModel.save()

        transaction.objects.create(username=currentUserModel, transactionType=transactionType, amount=amount)

    context = {
        'form': form,
    }

    return render(request, 'home.html', context)
        