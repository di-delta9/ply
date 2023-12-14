# Generated by Django 4.2.4 on 2023-12-07 16:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('community', '0011_alter_communitysidebarmenu_module'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityDashboardType',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dashboard_type', models.TextField(max_length=200, verbose_name='Dashboard Type Tag')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Updated')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.community', verbose_name='Community')),
            ],
            options={
                'db_table': 'communities_community_community_dashboard_type',
            },
        ),
        migrations.CreateModel(
            name='CommunityProfileDashboardRoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active FLAG')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.community', verbose_name='Community')),
                ('dasbhoard_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='community.communitydashboardtype', verbose_name='Dashboard Type')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='profiles.profile', verbose_name='User')),
            ],
            options={
                'db_table': 'communities_community_community_profile_dashboard_roles',
            },
        ),
    ]