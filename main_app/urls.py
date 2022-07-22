from django.urls import path
from .views import index, register, loginPage, homePage

urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('login', loginPage, name='login'),
    path('home', homePage, name='home'),
]