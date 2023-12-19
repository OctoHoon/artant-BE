# Generated by Django 4.2.3 on 2023-12-17 17:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Section",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=64)),
                ("order", models.PositiveIntegerField(default=1)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Shop",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_activated", models.BooleanField(default=False)),
                ("register_step", models.IntegerField(default=1)),
                ("avatar", models.URLField(blank=True, null=True)),
                ("background_pic", models.URLField(blank=True, null=True)),
                ("shop_name", models.CharField(max_length=256)),
                ("short_description", models.CharField(default="", max_length=256)),
                (
                    "description_title",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "description",
                    models.TextField(blank=True, max_length=2000, null=True),
                ),
                (
                    "announcement",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("expiration", models.DateField(blank=True, null=True)),
                ("cancellation", models.BooleanField(default=True)),
                (
                    "shop_policy_updated_at",
                    models.DateField(
                        blank=True, default=datetime.date.today, null=True
                    ),
                ),
                ("instagram_url", models.URLField(blank=True, null=True)),
                ("facebook_url", models.URLField(blank=True, null=True)),
                ("website_url", models.URLField(blank=True, null=True)),
                ("is_star_seller", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ShopVideo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("video", models.URLField()),
                (
                    "shop",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="video",
                        to="shops.shop",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ShopImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("image", models.URLField()),
                ("order", models.PositiveIntegerField()),
                (
                    "shop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="shops.shop",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
