# Generated by Django 4.0.2 on 2023-03-24 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_productitems_ordered'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ordered',
        ),
    ]
