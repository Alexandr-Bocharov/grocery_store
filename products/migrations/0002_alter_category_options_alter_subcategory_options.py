# Generated by Django 5.1.6 on 2025-02-20 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "категория", "verbose_name_plural": "категории"},
        ),
        migrations.AlterModelOptions(
            name="subcategory",
            options={"verbose_name": "категория", "verbose_name_plural": "категории"},
        ),
    ]
