# Generated by Django 4.0.4 on 2022-08-24 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0006_basestat_descr'),
        ('exp', '0008_alter_levelscript_classtype_alter_levelscript_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='levelscript',
            name='classtype',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='stats.classtype', verbose_name='Class Type'),
        ),
    ]
