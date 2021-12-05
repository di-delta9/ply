# Generated by Django 3.2.9 on 2021-11-14 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='approved_flag',
            field=models.BooleanField(default=False, verbose_name='Approved FLAG'),
        ),
        migrations.AlterField(
            model_name='friends',
            name='approved',
            field=models.DateTimeField(null=True, verbose_name='Approved?'),
        ),
        migrations.AlterField(
            model_name='friends',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Request Created'),
        ),
    ]
