# Generated by Django 3.2.9 on 2021-11-24 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_profile_slug'),
        ('group', '0003_auto_20211118_2043'),
        ('gallery', '0040_auto_20211124_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallerycollectionpermission',
            name='group_old',
        ),
        migrations.RemoveField(
            model_name='gallerycollectionpermission',
            name='profile_old',
        ),
        migrations.AddField(
            model_name='gallerycollectionpermission',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='group.group', verbose_name='Group'),
        ),
        migrations.AddField(
            model_name='gallerycollectionpermission',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='profiles.profile', verbose_name='Profile'),
        ),
    ]
