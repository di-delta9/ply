# Generated by Django 3.2.9 on 2021-11-18 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_profile_slug'),
        ('metrics', '0004_auto_20211118_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilepagehit',
            name='visitor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='profiles.profile', verbose_name='Viewed by Profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profilepagehit',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='profiles.profile', verbose_name='Parent'),
        ),
    ]
