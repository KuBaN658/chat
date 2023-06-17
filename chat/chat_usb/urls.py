from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('^$', views.index, name='index'),
    path(r'^contacts/$', views.UserListView.as_view(), name='contacts')
]