# Generated by Django 2.2.5 on 2021-07-10 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LogAndRegApp', '0003_auto_20210710_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wall_message',
            name='poster',
        ),
        migrations.RemoveField(
            model_name='wall_message',
            name='user_likes',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Wall_Message',
        ),
    ]