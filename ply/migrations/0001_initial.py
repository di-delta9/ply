# Generated by Django 4.2.4 on 2024-04-14 04:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PlyApplication",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "app_name",
                    models.TextField(blank=True, verbose_name="Application Name"),
                ),
                (
                    "app_module",
                    models.TextField(unique=True, verbose_name="Application Module"),
                ),
                (
                    "version_release",
                    models.TextField(
                        default="0", verbose_name="Application Module Release Version"
                    ),
                ),
                (
                    "version_major",
                    models.TextField(
                        default="0", verbose_name="Application Module Major Version"
                    ),
                ),
                (
                    "version_minor",
                    models.TextField(
                        default="0", verbose_name="Application Module Minor Version"
                    ),
                ),
                (
                    "installed",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Date Installed"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Date Updated"
                    ),
                ),
            ],
            options={
                "db_table": "ply_application",
            },
        ),
        migrations.CreateModel(
            name="PlyApplicationVersionHistory",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "old_version_string",
                    models.TextField(verbose_name="Application Old Version String"),
                ),
                (
                    "new_version_string",
                    models.TextField(verbose_name="Application New Version String"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Date Updated"),
                ),
                (
                    "application",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ply.plyapplication",
                        verbose_name="Ply Application",
                    ),
                ),
            ],
            options={
                "db_table": "ply_application_version_history",
            },
        ),
    ]
