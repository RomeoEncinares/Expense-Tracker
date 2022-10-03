from django.urls import path
from .views import index, register, loginView, homeView, transactionsView, statisticsView, statisticsBalanceView, statisticsCashFlowView, statisticsSpendingView

urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('login', loginView, name='login'),
    path('home', homeView, name='home'),
    path('transactions', transactionsView, name='transactions'),
    path('statistics', statisticsView, name='statistics'),
    path('statistics/balance/', statisticsBalanceView, name='statisticsBalance'),
    path('statistics/cashflow/', statisticsCashFlowView, name='statisticsCashFlow'),
    path('statistics/spending/', statisticsSpendingView, name='statisticsSpendingView'),

]