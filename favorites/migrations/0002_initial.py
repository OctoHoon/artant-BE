# Generated by Django 4.2.3 on 2024-01-12 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("favorites", "0001_initial"),
        ("shops", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="favoriteshop",
            name="shops",
            field=models.ManyToManyField(
                related_name="favorites_shop", to="shops.shop"
            ),
        ),
    ]
