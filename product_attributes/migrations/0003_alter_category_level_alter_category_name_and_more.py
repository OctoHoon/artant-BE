# Generated by Django 4.2.3 on 2023-12-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product_attributes", "0002_rename_tag_producttag_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="level",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name="color",
            name="name",
            field=models.CharField(
                choices=[
                    ("White", "White"),
                    ("Black", "Black"),
                    ("Blue", "Blue"),
                    ("Green", "Green"),
                    ("Gray", "Gray"),
                    ("Orange", "Orange"),
                    ("Purple", "Purple"),
                    ("Red", "Red"),
                    ("Brown", "Brown"),
                    ("Yellow", "Yellow"),
                    ("Gold", "Gold"),
                    ("Silver", "Silver"),
                    ("Colorful", "Colorful"),
                ],
                max_length=20,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="material",
            name="name",
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
