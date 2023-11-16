# Generated by Django 4.2.4 on 2023-08-15 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('page_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.TextField(max_length=200, verbose_name='Page slug')),
                ('label', models.TextField(max_length=200, verbose_name='Page Label')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Page Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Page Updated')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'db_table': 'core_dynapages_page',
            },
        ),
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_id', models.TextField(max_length=200, verbose_name='Template ID')),
                ('label', models.TextField(max_length=200, verbose_name='Template Label')),
                ('filename', models.TextField(max_length=200, verbose_name='Template Filename')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Template Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Template Updated')),
                ('creator', models.TextField(default='system', max_length=200, verbose_name='Creator')),
                ('description', models.TextField(default='a template page', max_length=2000, verbose_name='Description')),
                ('app', models.TextField(blank=True, default='', max_length=200, null=True, verbose_name='App Name ID')),
                ('archived', models.BooleanField(default=False, verbose_name='Archived FLAG')),
                ('blocked', models.BooleanField(default=False, verbose_name='Blocked FLAG')),
                ('page_template', models.BooleanField(default=True, verbose_name='Template is used for Pages')),
                ('widget_template', models.BooleanField(default=False, verbose_name='Template is used for Widgets')),
                ('frozen', models.BooleanField(default=False, verbose_name='Frozen FLAG')),
                ('system', models.BooleanField(default=False, verbose_name='System FLAG')),
            ],
            options={
                'db_table': 'core_dynapages_templates',
            },
        ),
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('widget_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('widget_id', models.TextField(default='', max_length=200, unique=True, verbose_name='Widget ID')),
                ('widget_name', models.TextField(default='', max_length=200, unique=True, verbose_name='Widget Name')),
                ('author', models.TextField(default='', max_length=200, verbose_name='Widget Author')),
                ('label', models.TextField(max_length=200, verbose_name='Widget Label')),
                ('descr', models.TextField(max_length=200, verbose_name='Widget Description')),
                ('helptext', models.TextField(max_length=200, verbose_name='Widget Helptext')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Widget Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Widget Updated')),
                ('version', models.TextField(max_length='20', verbose_name='Widget Vers')),
                ('plugin', models.TextField(default='', null=True, verbose_name='Widget Plugin')),
                ('widget_data', models.JSONField(blank=True, null=True, verbose_name='Widget plugin-specific data')),
                ('archived', models.BooleanField(default=False, verbose_name='Archived FLAG')),
                ('thumbnail', models.TextField(blank=True, null=True, verbose_name='Widget Thumbnail')),
                ('icon', models.TextField(blank=True, null=True, verbose_name='Widget Icon')),
                ('banner', models.BooleanField(default=False, verbose_name='Includes Banner Mode')),
                ('mainbody', models.BooleanField(default=True, verbose_name='Includes MainBody Mode')),
                ('sidecol', models.BooleanField(default=False, verbose_name='Includes SideColumn Mode')),
                ('footer', models.BooleanField(default=False, verbose_name='Includes Footer Mode')),
                ('profile', models.BooleanField(default=False, verbose_name='Includes Profile Mode')),
                ('SLHUD', models.BooleanField(default=False, verbose_name='Includes SLHUD Mode')),
                ('group', models.BooleanField(default=True, verbose_name='Includes Group Mode')),
                ('dashboard', models.BooleanField(default=False, verbose_name='Includes Dashboard Mode')),
                ('blog', models.BooleanField(default=False, verbose_name='Includes Blog Mode')),
                ('app', models.TextField(blank=True, default='', max_length=200, null=True, verbose_name='App Name ID')),
                ('setup_form', models.TextField(blank=True, default='', max_length=200, null=True, verbose_name='Setup Form Class Name')),
                ('setup_required', models.BooleanField(default=False, verbose_name='Setup Required')),
                ('blocked', models.BooleanField(default=False, verbose_name='Blocked FLAG')),
                ('frozen', models.BooleanField(default=False, verbose_name='Frozen FLAG')),
                ('system', models.BooleanField(default=False, verbose_name='System FLAG')),
                ('active', models.BooleanField(default=True, verbose_name='Active FLAG')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynapages.templates', verbose_name='Dynapage Template')),
            ],
            options={
                'db_table': 'core_dynapages_widgets',
            },
        ),
        migrations.CreateModel(
            name='PageWidget',
            fields=[
                ('pagewidget_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Widget Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Widget Updated')),
                ('banner', models.BooleanField(default=False, verbose_name='Banner Mode')),
                ('mainbody', models.BooleanField(default=False, verbose_name='MainBody Mode')),
                ('sidecol', models.BooleanField(default=False, verbose_name='SideColumn Mode')),
                ('footer', models.BooleanField(default=False, verbose_name='Footer Mode')),
                ('pos', models.TextField(blank=True, max_length=200, null=True, verbose_name='Widget Position (Column)')),
                ('order', models.IntegerField(default=0, verbose_name='Widget Order')),
                ('thumbnail', models.TextField(blank=True, default='', null=True, verbose_name='Widget Thumbnail')),
                ('plugin_data', models.JSONField(blank=True, null=True, verbose_name='Widget plugin-specific data')),
                ('active', models.BooleanField(default=True, verbose_name='Active FLAG')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynapages.page', verbose_name='DynaPage')),
                ('widget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynapages.widget', verbose_name='Widget')),
            ],
            options={
                'db_table': 'core_dynapages_page_widget',
            },
        ),
        migrations.AddField(
            model_name='page',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynapages.templates', verbose_name='Dynapage Template'),
        ),
    ]