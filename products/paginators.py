from rest_framework.pagination import PageNumberPagination


class CategoryPagination(PageNumberPagination):
    """Пагинация для модели CategoryListAPIView"""

    page_size = 1
    page_size_query_param = "page_size"
    max_page_size = 100


class ProductPagination(PageNumberPagination):
    """Пагинация для модели ProductListAPIView"""

    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 50
