# Generated by Django 2.2.5 on 2021-07-17 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E2BlackApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='users_who_like',
            field=models.ManyToManyField(related_name='liked_books', to='E2BlackApp.User'),
        ),
    ]