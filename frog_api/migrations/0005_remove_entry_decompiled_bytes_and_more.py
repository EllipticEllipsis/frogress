# Generated by Django 4.1 on 2022-08-22 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("frog_api", "0004_alter_category_options_alter_entry_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="entry",
            name="decompiled_bytes",
        ),
        migrations.RemoveField(
            model_name="entry",
            name="decompiled_chunks",
        ),
        migrations.RemoveField(
            model_name="entry",
            name="matching_bytes",
        ),
        migrations.RemoveField(
            model_name="entry",
            name="matching_chunks",
        ),
        migrations.RemoveField(
            model_name="entry",
            name="total_bytes",
        ),
        migrations.RemoveField(
            model_name="entry",
            name="total_chunks",
        ),
    ]
