from carts.apps import CartsConfig
from rest_framework.urls import path

from carts.views import (
    CartAPIView,
    CartAddAPIView,
    CartItemUpdateAPIView,
    CartItemDeleteAPIView,
    CartClearAPIView,
)

app_name = CartsConfig.name

urlpatterns = [
    path("detail/", CartAPIView.as_view(), name="cart-detail"),
    path("add_cart_item/", CartAddAPIView.as_view(), name="add-cart-item"),
    path(
        "cart_item_update/<int:pk>/",
        CartItemUpdateAPIView.as_view(),
        name="cart-item-update",
    ),
    path(
        "cart_item_delete/<int:pk>/",
        CartItemDeleteAPIView.as_view(),
        name="cart-item-delete",
    ),
    path("cart_clear/", CartClearAPIView.as_view(), name="cart-clear"),
]
