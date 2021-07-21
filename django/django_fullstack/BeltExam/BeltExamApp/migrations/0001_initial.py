# Generated by Django 2.2.5 on 2021-07-17 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('description', models.CharField(default='Text', max_length=255)),
                ('granted_wish', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Robert', max_length=255)),
                ('last_name', models.CharField(default='Johnson', max_length=255)),
                ('email', models.CharField(default='kuyperhouse@gmail.com', max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to='BeltExamApp.User')),
                ('wall_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='BeltExamApp.Books')),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_messages', to='BeltExamApp.User'),
        ),
        migrations.AddField(
            model_name='books',
            name='user_who_grants',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wish_granted', to='BeltExamApp.User'),
        ),
        migrations.AddField(
            model_name='books',
            name='users_who_like',
            field=models.ManyToManyField(related_name='liked_books', to='BeltExamApp.User'),
        ),
    ]
