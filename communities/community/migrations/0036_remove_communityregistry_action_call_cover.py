# Generated by Django 5.0.1 on 2024-05-12 18:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("community", "0035_communityregistry_foreign_key_ref"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="communityregistry",
            name="action_call_cover",
        ),
    ]
