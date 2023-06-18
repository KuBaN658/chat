from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import User, Message, Chat
from django.views.generic import ListView, DetailView


def index(request):
    """
    Функция отображения добашней страницы сайта
    """
    num_messages = Message.objects.all().count()
    num_user = User.objects.all().count()
    num_chat = Chat.objects.all().count()
    return render(
        request,
        'chat_usb/index.html',
        context={
            'num_messages': num_messages,
            'num_user': num_user,
            'num_chat': num_chat,
        }
    )

class UserListView(ListView):
    model = User

    def get_queryset(self):
        return User.objects.all()

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(UserListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        context['some_data'] = 'This is just some data'
        return context


class UserDetailView(DetailView):
    template_name = 'chat_usb/user_detail.html'
    model = User
    context_object_name = 'user'
