# Generated by Django 4.1.3 on 2022-11-22 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("protected_dashboard", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="result",
            name="is_passed",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
