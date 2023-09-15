
from django.urls import path
from app_meu_primeiro_app import views

urlpatterns = [
    path('', views.home, name='teste'),
]
