# Generated by Django 2.2 on 2021-06-26 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BJ1app', '0002_auto_20210626_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=25),
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='email_address',
            field=models.EmailField(default='robert@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='Johnson', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='Robert', max_length=255),
        ),
    ]
