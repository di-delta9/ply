# Generated by Django 3.2.9 on 2021-11-18 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0006_galleryitemhittotals_grouppagehittotals_profilepagehittotals'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryitemhittotals',
            name='type',
            field=models.TextField(db_index=True, default='', verbose_name='Hit Type'),
            preserve_default=False,
        ),
    ]
