# Generated by Django 3.1.6 on 2021-02-07 19:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20210207_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquiz',
            name='quiz_user_created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
