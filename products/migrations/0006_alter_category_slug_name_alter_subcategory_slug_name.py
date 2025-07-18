# Generated by Django 5.1.6 on 2025-02-21 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_alter_category_slug_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug_name",
            field=models.SlugField(
                blank=True,
                help_text="поле заполняется автоматически",
                null=True,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="subcategory",
            name="slug_name",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
