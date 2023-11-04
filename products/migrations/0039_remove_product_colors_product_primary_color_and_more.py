# Generated by Django 4.2.3 on 2023-11-01 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0038_material_productmaterial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="colors",
        ),
        migrations.AddField(
            model_name="product",
            name="primary_color",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="primary_color_products",
                to="products.color",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="secondary_color",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="secondary_color_products",
                to="products.color",
            ),
        ),
    ]
