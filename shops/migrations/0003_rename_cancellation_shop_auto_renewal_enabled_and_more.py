# Generated by Django 4.2.3 on 2023-12-18 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shops", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="shop",
            old_name="cancellation",
            new_name="auto_renewal_enabled",
        ),
        migrations.RenameField(
            model_name="shop",
            old_name="expiration",
            new_name="subscription_expiration_date",
        ),
        migrations.AlterField(
            model_name="section",
            name="order",
            field=models.PositiveIntegerField(),
        ),
    ]
