# Generated by Django 4.1.1 on 2022-09-19 13:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=100)),
                ("gender", models.CharField(max_length=6)),
                ("location", models.CharField(max_length=100)),
                ("regDate", models.DateField(default=datetime.datetime.today)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("quantity", models.IntegerField(default=1)),
                ("price", models.IntegerField()),
                ("address", models.CharField(blank=True, default="", max_length=50)),
                ("phone", models.CharField(blank=True, default="", max_length=50)),
                ("date", models.DateField(default=datetime.datetime.today)),
                ("status", models.BooleanField(default=False)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.customer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ShippingDetails",
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
                ("Address", models.CharField(blank=True, default="", max_length=50)),
                ("State", models.CharField(blank=True, default="", max_length=50)),
                ("City", models.DateField(blank=True, default="", max_length=50)),
                ("Pincode", models.IntegerField()),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.customer",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="customer.order"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Products",
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
                ("name", models.CharField(max_length=60)),
                ("price", models.IntegerField(default=0)),
                (
                    "description",
                    models.CharField(blank=True, default="", max_length=250, null=True),
                ),
                (
                    "image",
                    models.ImageField(upload_to="static/Assets/images/products/"),
                ),
                ("likes", models.IntegerField(default=0)),
                (
                    "category",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.category",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="customer.products"
            ),
        ),
    ]
