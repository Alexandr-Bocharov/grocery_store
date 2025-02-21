from django.shortcuts import render
from rest_framework import generics
from products.serializers import CategorySerializer
from products.models import Category
from products.paginators import CategoryPagination


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CategoryPagination

