# Generated by Django 5.1.6 on 2025-02-22 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0013_alter_product_image1_alter_product_image2_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ImageField(upload_to=""),
        ),
        migrations.AlterField(
            model_name="product",
            name="image1",
            field=models.ImageField(upload_to=""),
        ),
        migrations.AlterField(
            model_name="product",
            name="image2",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="product",
            name="image3",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="subcategory",
            name="image",
            field=models.ImageField(upload_to=""),
        ),
    ]
