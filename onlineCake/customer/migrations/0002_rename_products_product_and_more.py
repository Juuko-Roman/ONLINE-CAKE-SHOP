# Generated by Django 4.1.1 on 2022-09-19 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="Products", new_name="Product",),
        migrations.RenameModel(old_name="ShippingDetails", new_name="ShippingDetail",),
    ]
