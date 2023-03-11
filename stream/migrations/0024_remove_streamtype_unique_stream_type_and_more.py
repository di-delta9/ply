# Generated by Django 4.0.4 on 2022-08-31 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_alter_communityprofile_profile'),
        ('stream', '0023_alter_stream_streamtype'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='streamtype',
            name='unique_stream_type',
        ),
        migrations.AddField(
            model_name='streamtype',
            name='community',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='community.community', verbose_name='Community'),
        ),
        migrations.AddConstraint(
            model_name='streamtype',
            constraint=models.UniqueConstraint(fields=('name', 'community'), name='unique_stream_type'),
        ),
    ]