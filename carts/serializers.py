from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from carts.models import Cart, CartItem
from products.models import Product
from products.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели CartItem """

    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ("id", "quantity", "product")


class CartSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Cart """
    cart_items = CartItemSerializer(many=True)
    total_price = serializers.SerializerMethodField()
    total_quantity = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ("cart_items", "total_price", "total_quantity")

    def get_total_price(self, obj):
        return obj.total_price()

    def get_total_quantity(self, obj):
        return obj.total_quantity()


class CartItemCreateUpdateSerializer(serializers.ModelSerializer):
    """ Сериализатор для контроллера CartAddAPIView """
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CartItem
        fields = ("product_id", "quantity")

    def validate_product_id(self, value):
        if not Product.objects.filter(id=value).exists():
            raise ValidationError("Продукта с таким ID не существует")
        return value


class CartItemProductCounterSerializer(serializers.ModelSerializer):
    """ Сериализатор для контроллера CartItemUpdateAPIView """
    product_id = serializers.IntegerField(write_only=True)
    quantity = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ("product_id", "quantity")
