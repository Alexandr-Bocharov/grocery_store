from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from products.models import Category, Product


class SubcategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ("name", "slug_name",)


class CategorySerializer(ModelSerializer):
    subcategories = SubcategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ("name", "slug_name", "subcategories")


class ProductSerializer(ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("name", "slug_name", "category", "subcategory", "price", "images")

    def get_images(self, obj):
        """Собираем все изображения в список."""
        return [img.url for img in [obj.image1, obj.image2, obj.image3] if img]
