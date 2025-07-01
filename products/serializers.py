from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from products.models import Category, Product


class SubcategorySerializer(ModelSerializer):
    """Сериализатор для модели Subcategory"""

    class Meta:
        model = Category
        fields = (
            "name",
            "slug_name",
        )


class CategorySerializer(ModelSerializer):
    """Сериализатор для модели Category"""

    subcategories = SubcategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ("name", "slug_name", "subcategories")


class ProductSerializer(ModelSerializer):
    """Сериализатор для модели Product"""

    images = serializers.SerializerMethodField()
    category = serializers.StringRelatedField()
    subcategory = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "slug_name",
            "category",
            "subcategory",
            "price",
            "images",
        )

    def get_images(self, obj):
        """Собираем все изображения в список"""
        return [img.url for img in [obj.image1, obj.image2, obj.image3] if img]
