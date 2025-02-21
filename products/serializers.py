from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from products.models import Category


class SubcategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ("name", "slug_name",)


class CategorySerializer(ModelSerializer):
    subcategories = SubcategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ("name", "slug_name", "subcategories")


