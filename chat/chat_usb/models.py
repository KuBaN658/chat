from django.db import models
from django.urls import reverse


class Message(models.Model):
    """
    Модель описывающая сообщения
    """
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)
    text = models.CharField(max_length=200, help_text="Введите сообщение")
    date_create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class Chat(models.Model):
    """
    Модель описывающая чат
    """
    user1 = models.ForeignKey('User',
                              related_name='first',
                              on_delete=models.CASCADE,
                              null=True
                              )
    user2 = models.ForeignKey('User',
                              related_name='second',
                              on_delete=models.CASCADE,
                              null=True
                              )

    def __str__(self):
        return f"idchat#{self.pk}"


class User(models.Model):
    """
    Модель описывающая пользователя
    """
    username = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])


