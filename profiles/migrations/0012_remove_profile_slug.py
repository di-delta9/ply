# Generated by Django 3.2.9 on 2021-11-17 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20211117_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
    ]
