# Generated by Django 4.0.4 on 2023-03-26 19:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import registration.models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0037_alter_application_closedate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='closeDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 26, 19, 14, 22, 204597, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='application',
            name='openDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 26, 19, 14, 22, 204578, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='aaClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 26, 19, 14, 22, 203837, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='aaOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 26, 19, 14, 22, 203827, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='dealersClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 26, 19, 14, 22, 203816, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='dealersOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 26, 19, 14, 22, 203796, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventsClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 26, 19, 14, 22, 203858, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventsOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 26, 19, 14, 22, 203847, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 26, 19, 14, 22, 203761, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regEditClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 26, 19, 14, 22, 203784, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regEditOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 26, 19, 14, 22, 203773, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 26, 19, 14, 22, 203738, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='webconnexaction',
            name='id',
            field=models.CharField(default=registration.models.StringKeyGenerator.__call__, max_length=64, primary_key=True, serialize=False, unique=True),
        ),
    ]