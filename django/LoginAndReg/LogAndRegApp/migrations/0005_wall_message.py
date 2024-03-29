# Generated by Django 2.2.5 on 2021-07-10 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LogAndRegApp', '0004_auto_20210710_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wall_Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_messages', to='LogAndRegApp.User')),
                ('user_likes', models.ManyToManyField(related_name='liked_posts', to='LogAndRegApp.User')),
            ],
        ),
    ]
