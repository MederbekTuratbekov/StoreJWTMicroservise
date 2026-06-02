from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer


class CartView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartSerializer

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(
            user_id=request.user.id
        )
        serializer = self.get_serializer(cart)
        return Response(serializer.data)


class CartItemViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(
            cart__user_id=self.request.user.id
        )

    def perform_create(self, serializer):
        cart, _ = Cart.objects.get_or_create(
            user_id=self.request.user.id
        )
        serializer.save(cart=cart)
