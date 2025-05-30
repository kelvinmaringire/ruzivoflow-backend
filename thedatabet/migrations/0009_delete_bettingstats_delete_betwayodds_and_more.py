# Generated by Django 4.2.11 on 2025-04-04 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("thedatabet", "0008_thedatabet"),
    ]

    operations = [
        migrations.DeleteModel(
            name="BettingStats",
        ),
        migrations.DeleteModel(
            name="BetwayOdds",
        ),
        migrations.RenameField(
            model_name="bettingtips",
            old_name="games",
            new_name="tips",
        ),
        migrations.RemoveField(
            model_name="bettingtips",
            name="guest_sc_mse",
        ),
        migrations.RemoveField(
            model_name="bettingtips",
            name="guest_sc_r2",
        ),
        migrations.RemoveField(
            model_name="bettingtips",
            name="host_sc_mse",
        ),
        migrations.RemoveField(
            model_name="bettingtips",
            name="host_sc_r2",
        ),
        migrations.RemoveField(
            model_name="bettingtips",
            name="result_mse",
        ),
        migrations.RemoveField(
            model_name="bettingtips",
            name="result_r2",
        ),
    ]
