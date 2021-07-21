# Generated by Django 2.2.5 on 2021-07-15 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BeltReviewerApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='reviewer',
            field=models.ForeignKey(default='Text', on_delete=django.db.models.deletion.CASCADE, related_name='user_reviews', to='BeltReviewerApp.User'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='review',
            field=models.CharField(default='Text', max_length=255),
        ),
    ]
