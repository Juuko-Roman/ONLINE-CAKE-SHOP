# Generated by Django 4.1.1 on 2022-09-29 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0011_alter_order_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order", old_name="paymentMethod", new_name="payMethod",
        ),
    ]
