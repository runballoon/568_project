# Generated by Django 4.1.6 on 2023-05-06 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="stocks",
            name="update_time",
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
