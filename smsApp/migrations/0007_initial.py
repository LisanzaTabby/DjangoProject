# Generated by Django 5.0.6 on 2024-05-27 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('smsApp', '0006_delete_userinfor'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
