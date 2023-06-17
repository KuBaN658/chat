from django.contrib import admin
from .models import User, Message, Chat


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    list_filter = ()


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'chat', 'text', 'date_create')
    list_filter = ()
    fieldsets = (
        (None, {
            'fields': ('text',)
        }),
        ('содержание', {
            'fields': ('user', 'chat',)
        })
    )


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'user1', 'user2')
    list_filter = ()
    fields = [('user1', 'user2')]