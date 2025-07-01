from rest_framework import views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from carts.models import Cart, CartItem
from carts.serializers import CartSerializer, CartItemSerializer
from carts.serializers import (
    CartItemCreateUpdateSerializer,
    CartItemProductCounterSerializer,
)


class CartAPIView(views.APIView):
    """Получение товаров, добавленных в корзину"""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(
            user=request.user
        )  # если корзины нет - создаем ее

        serializer = CartSerializer(cart)
        return Response(serializer.data)


class CartAddAPIView(views.APIView):
    """Добавление товара в корзину"""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CartItemCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data.get("product_id")
            quantity = serializer.validated_data.get("quantity", 1)

            cart, _ = Cart.objects.get_or_create(user=request.user)

            cart_item, created = CartItem.objects.get_or_create(
                cart=cart, product_id=product_id
            )

            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity

            cart_item.save()

            return Response(
                CartItemSerializer(cart_item).data, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartItemUpdateAPIView(views.APIView):
    """Изменение количества товара в корзине"""

    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            cart_item = CartItem.objects.get(pk=pk, cart__user=request.user)
        except CartItem.DoesNotExist:
            return Response(
                {"ошибка": "Товар не найден в вашей корзине"},
                status=status.HTTP_404_NOT_FOUND,
            )
        data = request.data
        data["product_id"] = (
            cart_item.product.id
        )  # чтобы не передавать product_id в теле запроса

        serializer = CartItemProductCounterSerializer(data=data)
        if serializer.is_valid():
            cart_item.quantity = serializer.validated_data.get("quantity")

            if cart_item.quantity > 0:
                cart_item.save()
                return Response(
                    CartItemSerializer(cart_item).data, status=status.HTTP_200_OK
                )
            else:
                cart_item.delete()
                return Response(
                    {
                        "message": "Товар удален из корзины, так как счетчик товара был установлен на 0"
                    },
                    status=status.HTTP_204_NO_CONTENT,
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartItemDeleteAPIView(views.APIView):
    """Удаление товара из корзины"""

    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        try:
            cart_item = CartItem.objects.get(pk=pk, cart__user=request.user)
            cart_item.delete()
            return Response(
                {"message": "Товар успешно удален из вашей корзины"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except CartItem.DoesNotExist:
            return Response(
                {"ошибка": "Товар не найден в вашей корзине"},
                status=status.HTTP_404_NOT_FOUND,
            )


class CartClearAPIView(views.APIView):
    """Удаление всех товаров из корзины"""

    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)

        cart.cart_items.all().delete()

        return Response(
            {"message": "Корзина успешно очищена."}, status=status.HTTP_204_NO_CONTENT
        )
