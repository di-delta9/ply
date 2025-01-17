# Generated by Django 5.0.1 on 2024-12-30 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0047_alter_communitysidebarmenu_module'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitysidebarmenu',
            name='module',
            field=models.TextField(choices=[('communities.preferences', 'communities.preferences'), ('communities.community', 'communities.community'), ('communities.dashboards', 'communities.dashboards'), ('media.gallery.core', 'media.gallery.core'), ('ufls.front', 'ufls.front'), ('ufls.event', 'ufls.event'), ('ufls.registrar', 'ufls.registrar'), ('ufls.dealers', 'ufls.dealers'), ('ufls.scheduling', 'ufls.scheduling'), ('ufls.staff', 'ufls.staff')], help_text='Application to Include in the Menus', max_length=200, verbose_name='Module/AppName:'),
        ),
    ]
