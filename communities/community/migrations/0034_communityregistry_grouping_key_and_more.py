# Generated by Django 5.0.1 on 2024-05-11 02:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("community", "0033_communityregistry_uuid_value"),
    ]

    operations = [
        migrations.AddField(
            model_name="communityregistry",
            name="grouping_key",
            field=models.TextField(
                blank=True,
                max_length=200,
                null=True,
                verbose_name="Setting Grouping key",
            ),
        ),
        migrations.AlterField(
            model_name="communityregistry",
            name="key",
            field=models.TextField(max_length=400, verbose_name="Setting key"),
        ),
        migrations.AddIndex(
            model_name="communityregistry",
            index=models.Index(
                fields=["grouping_key"], name="communities_groupin_3a1df0_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="communityregistry",
            index=models.Index(fields=["key"], name="communities_key_571068_idx"),
        ),
        migrations.AddIndex(
            model_name="communityregistry",
            index=models.Index(
                fields=["grouping_key", "key"], name="communities_groupin_4a0115_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="communityregistry",
            index=models.Index(
                fields=["community"], name="communities_communi_f5229c_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="communityregistry",
            index=models.Index(
                fields=["grouping_key", "key", "community"],
                name="communities_groupin_1e7a9e_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="communityregistry",
            index=models.Index(
                fields=["community", "key"], name="communities_communi_3c8890_idx"
            ),
        ),
    ]