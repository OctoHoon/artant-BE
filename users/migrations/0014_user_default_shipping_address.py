# Generated by Django 4.2.3 on 2023-12-17 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0013_user_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="default_shipping_address",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="users.address",
            ),
        ),
    ]
