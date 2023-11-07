# Generated by Django 4.2.3 on 2023-11-06 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0048_product_is_active"),
        ("cart", "0018_alter_cartline_product_variant"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartline",
            name="product",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cartlines",
                to="products.product",
            ),
            preserve_default=False,
        ),
    ]
