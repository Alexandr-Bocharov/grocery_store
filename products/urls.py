from products.views import CategoryListAPIView, ProductListAPIView
from django.urls import path
from products.apps import ProductsConfig

app_name = ProductsConfig.name

urlpatterns = [
    path("category_list/", CategoryListAPIView.as_view(), name="category-list"),
    path("product_list/", ProductListAPIView.as_view(), name="product-list"),
]
