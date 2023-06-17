from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView


def chat(request):
    return HttpResponse('Здесь будет чат')

