# Generated by Django 4.0.4 on 2023-03-26 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0007_dealer_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealer',
            name='upgr_flag',
            field=models.BooleanField(default=False, help_text='Using their backup table size, percentage discount applied.'),
        ),
    ]