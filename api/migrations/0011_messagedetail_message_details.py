# Generated by Django 5.0.2 on 2024-02-18 08:12

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0010_remove_message_message_detail_delete_messagedetail"),
    ]

    operations = [
        migrations.CreateModel(
            name="MessageDetail",
            fields=[
                (
                    "message_detail_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("detail", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["updated_at", "created_at"],
            },
        ),
        migrations.AddField(
            model_name="message",
            name="details",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.messagedetail",
            ),
            preserve_default=False,
        ),
    ]