# Generated by Django 4.1.6 on 2023-05-06 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0003_overview_stocks_current_stocks_one_pred_diff_and_more"),
    ]

    operations = [
        migrations.RenameModel(old_name="Overview", new_name="Overviews",),
    ]