# Generated by Django 4.1.1 on 2022-09-22 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0002_rename_products_product_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                upload_to="customer/static/Assets/images/products/"
            ),
        ),
    ]
