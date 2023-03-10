# Generated by Django 4.0.2 on 2022-12-19 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('dateRegistered', models.DateTimeField(auto_now_add=True, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Customer Details',
            },
        ),
    ]
