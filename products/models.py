from django.db import models
from utils import NULLABLE


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug_name = models.SlugField()
    image = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Subcategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug_name = models.SlugField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
