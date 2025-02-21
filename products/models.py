from django.db import models
from utils import NULLABLE
from slugify import slugify


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug_name = models.SlugField(unique=True, **NULLABLE, help_text="поле заполняется автоматически")
    image = models.ImageField()

    def save(self, *args, **kwargs):
        self.slug_name = slugify(str(self.name))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Subcategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug_name = models.SlugField(unique=True, **NULLABLE, help_text="поле заполняется автоматически")
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")

    def save(self, *args, **kwargs):
        self.slug_name = slugify(str(self.name))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "подкатегория"
        verbose_name_plural = "подкатегории"
