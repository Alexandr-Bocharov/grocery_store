from django.db import models
from utils import NULLABLE
from slugify import slugify
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="наименование")
    slug_name = models.SlugField(
        unique=True,
        **NULLABLE,
        help_text="поле заполняется автоматически",
        verbose_name="slug-имя"
    )
    image = models.ImageField(verbose_name="изображение")

    def save(self, *args, **kwargs):
        self.slug_name = slugify(
            str(self.name)
        )  # переводим наименование категории в slug-значение
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Subcategory(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="наименование")
    slug_name = models.SlugField(
        unique=True,
        **NULLABLE,
        help_text="поле заполняется автоматически",
        verbose_name="slug-имя"
    )
    image = models.ImageField(verbose_name="изображение")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories",
        verbose_name="категория",
    )

    def save(self, *args, **kwargs):
        self.slug_name = slugify(
            str(self.name)
        )  # переводим наименование подкатегории в slug-значение
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "подкатегория"
        verbose_name_plural = "подкатегории"


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="наименование")
    slug_name = models.SlugField(
        unique=True,
        **NULLABLE,
        help_text="поле заполняется автоматически",
        verbose_name="slug-имя"
    )
    image1 = models.ImageField(verbose_name="изображение 200*200")
    image2 = models.ImageField(**NULLABLE, verbose_name="изображение 400*400")
    image3 = models.ImageField(**NULLABLE, verbose_name="изображение 600*600")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="цена")
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        verbose_name="подкатегория",
        related_name="products",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="категория",
        related_name="products",
    )

    def save(self, *args, **kwargs):
        self.slug_name = slugify(
            str(self.name)
        )  # переводим наименование продукта в slug-значение
        super().save(*args, **kwargs)

        if self.image1:  # если добавлено изображение делаем его размером 200 на 200
            img1 = Image.open(self.image1.path)
            img1.thumbnail((200, 200))
            img1.save(self.image1.path)

        if self.image2:  # если добавлено изображение делаем его размером 400 на 400
            img2 = Image.open(self.image2.path)
            img2.thumbnail((400, 400))
            img2.save(self.image2.path)

        if self.image3:  # если добавлено изображение делаем его размером 600 на 600
            img3 = Image.open(self.image3.path)
            img3.thumbnail((600, 600))
            img3.save(self.image3.path)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
