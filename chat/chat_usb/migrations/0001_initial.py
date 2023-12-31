# Generated by Django 4.2.2 on 2023-06-17 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Введите сообщение', max_length=200)),
                ('date_create', models.DateTimeField(auto_now=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat_usb.chat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat_usb.user')),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='user1',
            field=models.ManyToManyField(related_name='first', to='chat_usb.user'),
        ),
        migrations.AddField(
            model_name='chat',
            name='user2',
            field=models.ManyToManyField(related_name='second', to='chat_usb.user'),
        ),
    ]
