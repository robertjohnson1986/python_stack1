# Generated by Django 2.2.5 on 2021-07-13 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ZackProjectApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Giraffe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('catchphrase', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='giraffes_owned', to='ZackProjectApp.User')),
            ],
        ),
    ]