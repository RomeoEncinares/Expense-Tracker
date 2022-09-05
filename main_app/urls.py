from django.urls import path
from .views import index, register, loginPage, homeView

urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('login', loginPage, name='login'),
    path('home', homeView, name='home'),
]