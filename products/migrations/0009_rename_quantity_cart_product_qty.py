# Generated by Django 4.0.2 on 2022-12-24 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_cart_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='quantity',
            new_name='product_qty',
        ),
    ]