# Generated by Django 2.2.5 on 2021-07-17 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('E2BlackApp', '0003_auto_20210717_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='user_who_grants',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wish_granted', to='E2BlackApp.User'),
        ),
    ]
