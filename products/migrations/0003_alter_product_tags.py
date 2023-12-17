# Generated by Django 4.2.3 on 2023-12-17 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product_attributes", "0001_initial"),
        ("products", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="tags",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="products",
                to="product_attributes.producttag",
            ),
        ),
    ]
