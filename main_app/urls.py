from django.urls import path
from .views import index, register, loginView, homeView, transactionsView, statisticsView

urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('login', loginView, name='login'),
    path('home', homeView, name='home'),
    path('transactions', transactionsView, name='transactions'),
    path('statistics', statisticsView, name='statistics'),
]