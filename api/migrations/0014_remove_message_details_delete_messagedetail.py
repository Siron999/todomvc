# Generated by Django 5.0.2 on 2024-02-18 08:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0013_alter_message_details_alter_message_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="details",
        ),
        migrations.DeleteModel(
            name="MessageDetail",
        ),
    ]