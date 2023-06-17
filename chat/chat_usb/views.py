from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import User, Message, Chat


def index(request):
    """
    Функция отображения добашней страницы сайта
    """
    num_messages = Message.objects.all().count()
    num_user = User.objects.all().count()
    num_chat = Chat.objects.all().count()
    return render(
        request,
        'index.html',
        context={
            'num_messages': num_messages,
            'num_user': num_user,
            'num_chat': num_chat,
        }
    )
