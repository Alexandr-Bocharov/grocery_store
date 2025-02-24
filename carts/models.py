from django.db import models
from products.models import Product
from users.models import User


class Cart(models.Model):
    """ Модель корзины """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="пользователь"
    )

    class Meta:
        verbose_name = "корзина"
        verbose_name_plural = "корзины"

    def __str__(self):
        return f"корзина пользователя {self.user}"

    def total_price(self):
        """ Подсчет суммы всех товаров в корзине """
        return sum(item.total_price() for item in self.cart_items.all())

    def total_quantity(self):
        """ Подсчет количества всех товаров в корзине """
        return sum(item.quantity for item in self.cart_items.all())


class CartItem(models.Model):
    """ Модель товара в корзине """
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="cart_items",
        verbose_name="корзина",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product",
        verbose_name="продукт",
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "элемент корзины"
        verbose_name_plural = "элементы корзины"

    def __str__(self):
        return f"элемент корзины {self.cart}"

    def total_price(self):
        """ Подсчет суммы каждого CartItem(элемента корзины) """
        return self.product.price * self.quantity
