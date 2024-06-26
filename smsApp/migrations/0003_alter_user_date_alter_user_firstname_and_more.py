# Generated by Django 5.0.6 on 2024-05-21 08:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsApp', '0002_alter_user_email_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='firstname',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.TextField(max_length=100),
        ),
    ]
