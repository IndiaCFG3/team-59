from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
path('', views.home, name="home"),
path('scheme/', views.schemes),
path('register/', views.registerPage, name="register"),
path('login/', views.loginPage, name="login"),  
path('reset_password/', views.resetPassword, name="reset_password")
]