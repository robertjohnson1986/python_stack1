# Generated by Django 2.2.5 on 2021-07-14 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FavoriteBooksApp3', '0002_wall_message_users_who_like'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Wall_Message',
            new_name='Books',
        ),
    ]