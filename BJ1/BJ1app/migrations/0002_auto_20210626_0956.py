# Generated by Django 2.2 on 2021-06-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BJ1app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Wizard',
        ),
    ]
