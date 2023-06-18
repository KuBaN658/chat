from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.UserListView.as_view(), name='contacts'),
    path('contacts/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
]
