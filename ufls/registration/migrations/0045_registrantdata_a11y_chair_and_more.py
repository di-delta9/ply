# Generated by Django 4.2.4 on 2023-08-17 14:38

import datetime
from django.db import migrations, models
import registration.models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0044_alter_application_closedate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrantdata',
            name='a11y_chair',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registrantdata',
            name='a11y_elevator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registrantdata',
            name='a11y_eyesight',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registrantdata',
            name='a11y_full_assist',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registrantdata',
            name='a11y_group',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registrantdata',
            name='a11y_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registrantdata',
            name='a11y_partial_assist',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registrantdata',
            name='accessibility',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='closeDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 14, 38, 18, 329386, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='application',
            name='openDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 14, 38, 18, 329381, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='aaClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 14, 38, 18, 329095, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='aaOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 14, 38, 18, 329092, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='dealersClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 14, 38, 18, 329088, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='dealersOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 14, 38, 18, 329085, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventsClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 14, 38, 18, 329102, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventsOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 14, 38, 18, 329098, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 14, 38, 18, 329073, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regEditClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 14, 38, 18, 329081, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regEditOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 14, 38, 18, 329077, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 14, 38, 18, 329063, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='webconnexaction',
            name='id',
            field=models.CharField(default=registration.models.StringKeyGenerator.__call__, max_length=64, primary_key=True, serialize=False, unique=True),
        ),
    ]