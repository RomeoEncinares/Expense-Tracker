import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.db.models import Sum
from .models import userProfile, balanceRecord, transaction
from .forms import transactionForm, RegisterForm
from django.contrib.auth.decorators import login_required

def index(request):
    current_user = request.user
    print(current_user)
    return render(request, 'index.html')

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
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
            return redirect('home')
            
    return render(request, 'login.html')

@login_required
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

@login_required
def transactionsView(request):

    userObject = request.user
    userProfileModel = userProfile.objects.get(username=userObject)
    userTransactionsModel = transaction.objects.filter(username=userProfileModel)

    context = {
        'userTransactionsModel': userTransactionsModel,
    }
    
    return render(request, 'transactions.html', context)

@login_required
def statisticsView(request):
    
    context = {

    }
    
    return render(request, 'statistics.html', context)

@login_required
def statisticsBalanceView(request):

    userObject = request.user
    userProfileModel = userProfile.objects.get(username=userObject)
    balanceRecordModel = balanceRecord.objects.filter(username=userProfileModel)

    currentDate = datetime.datetime.now()
    sevenDays = currentDate - datetime.timedelta(days=7)
    thirdyDays = currentDate - datetime.timedelta(days=30)
    twelveWeeks = currentDate - datetime.timedelta(weeks=12)
    sixMonths = currentDate - datetime.timedelta(weeks=26)
    oneYear = currentDate - datetime.timedelta(weeks=52)

    sevenDaysBalanceRecord = balanceRecordModel.filter(date__range=(sevenDays, currentDate))
    thirtyDaysBalanceRecord = balanceRecordModel.filter(date__range=(thirdyDays, currentDate))
    twelveWeeksDaysBalanceRecord = balanceRecordModel.filter(date__range=(twelveWeeks, currentDate))
    sixMonthsDaysBalanceRecord = balanceRecordModel.filter(date__range=(sixMonths, currentDate))
    oneYearDaysBalanceRecord = balanceRecordModel.filter(date__range=(oneYear, currentDate))
    
    context = {
        'sevenDaysBalanceRecord': sevenDaysBalanceRecord,
        'thirtyDaysBalanceRecord': thirtyDaysBalanceRecord,
        'twelveWeeksDaysBalanceRecord': twelveWeeksDaysBalanceRecord,
        'sixMonthsDaysBalanceRecord': sixMonthsDaysBalanceRecord,
        'oneYearDaysBalanceRecord': oneYearDaysBalanceRecord,
    }
    
    return render(request, 'statistics-balance.html', context)       

@login_required
def statisticsCashFlowView(request):

    userObject = request.user
    userProfileModel = userProfile.objects.get(username=userObject)
    transactionRecordModel = transaction.objects.filter(username=userProfileModel)

    currentDate = datetime.datetime.now()
    sevenDays = currentDate - datetime.timedelta(days=7)
    thirdyDays = currentDate - datetime.timedelta(days=30)
    twelveWeeks = currentDate - datetime.timedelta(weeks=12)
    sixMonths = currentDate - datetime.timedelta(weeks=26)
    oneYear = currentDate - datetime.timedelta(weeks=52)

    sevenDaysTransactionRecord = transactionRecordModel.filter(date__range=(sevenDays, currentDate))
    thirtyDaysTransactionRecord = transactionRecordModel.filter(date__range=(thirdyDays, currentDate))
    twelveWeeksDaysTransactionRecord = transactionRecordModel.filter(date__range=(twelveWeeks, currentDate))
    sixMonthsDaysTransactionRecord = transactionRecordModel.filter(date__range=(sixMonths, currentDate))
    oneYearDaysTransactionRecord = transactionRecordModel.filter(date__range=(oneYear, currentDate))

    print(sevenDaysTransactionRecord)

    context = {
        'sevenDaysTransactionRecord': sevenDaysTransactionRecord,
        'thirtyDaysTransactionRecord': thirtyDaysTransactionRecord,
        'twelveWeeksDaysTransactionRecord': twelveWeeksDaysTransactionRecord,
        'sixMonthsDaysTransactionRecord': sixMonthsDaysTransactionRecord,
        'oneYearDaysTransactionRecord': oneYearDaysTransactionRecord,
    }

    return render(request, 'statistics-cashflow.html', context)

def statisticsSpendingView(request):

    userObject = request.user
    userProfileModel = userProfile.objects.get(username=userObject)
    ExpensetransactionRecordModel = transaction.objects.filter(username=userProfileModel, transactionType="Expense")

    ExpensesCategories = {
        'Food & Drinks': {},
        'Shopping': {},
        'Transportation': {},
        'Vehicle': {},
        'Life & Entertainment': {},
        'PC, Communication': {},
        'Financial Investment': {},
        'Investments': {},
        'Others': {},
    }

    currentDate = datetime.datetime.now()
    sevenDays = currentDate - datetime.timedelta(days=7)
    thirdyDays = currentDate - datetime.timedelta(days=30)
    twelveWeeks = currentDate - datetime.timedelta(weeks=12)
    sixMonths = currentDate - datetime.timedelta(weeks=26)
    oneYear = currentDate - datetime.timedelta(weeks=52)

    for category in ExpensesCategories:
        categoryQuery = ExpensetransactionRecordModel.filter(transactionCategory=category)
        expenseCategorySevenDaysSum = categoryQuery.filter(date__range=(sevenDays, currentDate)).aggregate(total=Sum('amount'))
        expenseCategoryThirtyDaysSum = categoryQuery.filter(date__range=(thirdyDays, currentDate)).aggregate(total=Sum('amount'))
        expenseCategoryTwekveWeeksSum = categoryQuery.filter(date__range=(twelveWeeks, currentDate)).aggregate(total=Sum('amount'))
        expenseCategorySixMonthsSum = categoryQuery.filter(date__range=(sixMonths, currentDate)).aggregate(total=Sum('amount'))
        expenseCategoryOneYearSum = categoryQuery.filter(date__range=(oneYear, currentDate)).aggregate(total=Sum('amount'))

        ExpensesCategories[category]['7D'] = expenseCategorySevenDaysSum['total']
        ExpensesCategories[category]['30D'] = expenseCategoryThirtyDaysSum['total']
        ExpensesCategories[category]['12W'] = expenseCategoryTwekveWeeksSum['total']
        ExpensesCategories[category]['6M'] = expenseCategorySixMonthsSum['total']
        ExpensesCategories[category]['1Y'] = expenseCategoryOneYearSum['total']
    
    context = {
        'ExpensesCategories': ExpensesCategories,
    }

    return render(request, 'statistics-spending.html', context)
