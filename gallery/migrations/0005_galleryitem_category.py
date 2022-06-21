# Generated by Django 4.0.4 on 2022-06-14 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_unique_hashdis'),
        ('gallery', '0004_alter_galleryitemcategory_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryitem',
            name='Category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='categories.category', verbose_name='Item Category'),
            preserve_default=False,
        ),
    ]