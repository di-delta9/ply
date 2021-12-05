# Generated by Django 3.2.9 on 2021-11-14 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_gallerycollectionitems_galleryitemfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryKeyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.TextField(max_length=200, verbose_name='Keyword')),
                ('hash', models.TextField(max_length=200, verbose_name='Hash')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Item Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='tem Updated')),
                ('items', models.IntegerField(default=0, verbose_name='Item Count')),
                ('views', models.IntegerField(default=0, verbose_name='Views Count')),
                ('likes', models.IntegerField(default=0, verbose_name='Likes Count')),
                ('shares', models.IntegerField(default=0, verbose_name='Shares Count')),
                ('comments', models.IntegerField(default=0, verbose_name='Comment Count')),
            ],
        ),
        migrations.AlterField(
            model_name='galleryitem',
            name='files',
            field=models.IntegerField(default=0, verbose_name='File Count'),
        ),
        migrations.CreateModel(
            name='GalleryItemKeywords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='Order Column')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('archived', models.BooleanField(default=False, verbose_name='Archived FLAG')),
                ('hidden', models.BooleanField(default=False, verbose_name='Hidden FLAG')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gallery.galleryitem', verbose_name='Item')),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gallery.gallerykeyword', verbose_name='keyword')),
            ],
        ),
    ]
