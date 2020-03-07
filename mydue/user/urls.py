from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    
    path('', views.Home(), name = 'home'),
    path('', views.RegView.as_view(), name = 'register'),
    path('', views.LoginView.as_view(), name = 'login'),
    path('', views.LogoutView.as_view(), name = 'logout'),

]