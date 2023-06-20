from django.urls import path, include
from . import views
from django.contrib.auth import urls

urlpatterns = [
    path('', include(urls)),
    path('dashboard', views.dashboard, name='dashboard')
]