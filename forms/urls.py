from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name='forms-welcome'),
    path('register/', views.register, name='forms-register'),
]
