from django.shortcuts import render
from rest_framework import generics
from products.serializers import CategorySerializer, ProductSerializer
from products.models import Category, Product
from products.paginators import CategoryPagination, ProductPagination




class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CategoryPagination


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPagination

