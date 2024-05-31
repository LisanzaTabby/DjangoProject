# Generated by Django 5.0.6 on 2024-05-28 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsApp', '0009_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='finance',
        ),
    ]
