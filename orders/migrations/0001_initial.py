# Generated by Django 4.1.6 on 2023-10-28 22:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "order_id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("status", models.CharField(max_length=255)),
            ],
        ),
    ]