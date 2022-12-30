# Generated by Django 4.0.2 on 2022-12-17 09:34

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_remove_product_category_delete_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('productImg', models.ImageField(blank=True, null=True, upload_to=products.models.get_file_path)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('status', models.BooleanField(default=False, help_text='0-default, 1-Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0-default, 1-Hidden')),
                ('meta_title', models.CharField(max_length=100)),
                ('meta_keywards', models.CharField(max_length=100)),
                ('meta_description', models.TextField(blank=True, max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slig', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to=products.models.get_file_path)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('small_description', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.BooleanField(default=False, help_text='0-default, 1-Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0-default, 1-Hidden')),
                ('tag', models.TextField(blank=True, max_length=500, null=True)),
                ('original_price', models.FloatField()),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('meta_title', models.CharField(max_length=100)),
                ('meta_keywards', models.CharField(max_length=100)),
                ('meta_description', models.TextField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
    ]