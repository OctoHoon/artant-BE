# Generated by Django 4.2.3 on 2023-11-01 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("purchases", "0003_alter_purchaseline_order_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="purchaseline",
            name="variant",
        ),
    ]
