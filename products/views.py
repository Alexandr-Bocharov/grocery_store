from rest_framework import generics
from products.serializers import CategorySerializer, ProductSerializer
from products.models import Category, Product
from products.paginators import CategoryPagination, ProductPagination


class CategoryListAPIView(generics.ListAPIView):
    """Получение списка всех категорий"""

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CategoryPagination


class ProductListAPIView(generics.ListAPIView):
    """Получение списка всех продуктов"""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPagination
