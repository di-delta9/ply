# Generated by Django 3.2.9 on 2021-11-18 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0026_galleryitem_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerytempfile',
            name='plugin',
            field=models.TextField(default='', verbose_name='File Plugin'),
            preserve_default=False,
        ),
    ]
