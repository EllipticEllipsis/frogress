# Generated by Django 4.1 on 2022-08-25 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("frog_api", "0006_alter_project_auth_key"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry",
            name="timestamp",
            field=models.IntegerField(),
        ),
    ]
