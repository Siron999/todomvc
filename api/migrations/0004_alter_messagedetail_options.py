# Generated by Django 5.0.2 on 2024-02-18 07:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_messagedetail"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="messagedetail",
            options={"ordering": ["created_at"]},
        ),
    ]