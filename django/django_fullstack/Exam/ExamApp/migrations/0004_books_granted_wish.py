# Generated by Django 2.2.5 on 2021-07-16 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamApp', '0003_auto_20210716_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='granted_wish',
            field=models.CharField(default='Text', max_length=255),
        ),
    ]
