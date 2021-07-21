# Generated by Django 2.2.5 on 2021-07-16 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='users_who_like',
        ),
        migrations.AddField(
            model_name='books',
            name='users_who_grant',
            field=models.ManyToManyField(null=True, related_name='granted_books', to='ExamApp.User'),
        ),
    ]