# Generated by Django 3.2.9 on 2021-11-14 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_rename_type_tickettype'),
        ('group', '0002_groupkeywords'),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined', models.DateTimeField(verbose_name='Joined')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.community', verbose_name='Community')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='profiles.profile', verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined', models.DateTimeField(verbose_name='Joined')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.community', verbose_name='Community')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='group.group', verbose_name='Group')),
            ],
        ),
    ]
