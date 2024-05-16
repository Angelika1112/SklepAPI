from ..models import * #import wytworzonych wcześniej klas modeli
from ..serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import uuid
from drf_yasg.utils import swagger_auto_schema

class CartTempClass:
    def __init__(self, cartId, itemlist):
        self.cartId = cartId
        self.itemList = itemlist
class CartApi(APIView):

    @swagger_auto_schema(responses={200: CartSerializer, 400: 'Bad Request'},
                         operation_description='Operacja zwraca zawartośść wybranego koszyka.')
    def get(self, request,cartId):
        cartItemList = CartItem.objects.filter(cartId=cartId)
        item = CartTempClass(cartId,[cartItem.itemId for cartItem in cartItemList])
        serializer = CartSerializer(item)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CartItemAddSerializer,
                         responses={200: CartItemAddSerializer, 400: 'Bad Request'},
                         operation_description='Operacja dodaje produkt do wybranego koszyka.')
    def post(self, request, cartId):
        serializer = CartItemAddSerializer(data=request.data)
        if serializer.is_valid():
            itemsNumber = int(serializer.validated_data['quantity'])
            for i in range(itemsNumber):
                cartItem = CartItem()
                cartItem.cartId = cartId
                cartItem.itemId = serializer.validated_data['itemId']
                cartItem.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=CartItemSerializer,
                         responses={204: 'No Content', 400: 'Bad Request'},
                         operation_description='Operacja usuwa produkt z wybranego koszyka.')
    def delete(self, request, cartId):
        serializer = CartItemSerializer(data=request.data)
        cartItemList = CartItem.objects.filter(cartId=cartId)
        if serializer.is_valid():
            itemsNumber = int(serializer.validated_data['quantity'])
            itemIdToRemove = int(serializer.validated_data['itemId'])
            for cartItem in cartItemList:
                if itemsNumber <= 0:
                    break
                if cartItem.itemId == itemIdToRemove:
                    cartItem.delete()
                    itemsNumber-=1
            return Response("Usunięto", status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartEmptyApi(APIView):

    @swagger_auto_schema(request_body=CartItemAddSerializer,
                         responses={200: CartItemAddSerializer, 400: 'Bad Request'},
                         operation_description='Operacja tworzy nowy koszyk i dodaje do niego produkt.')
    def post(self, request):
        serializer = CartItemAddSerializer(data=request.data)
        if serializer.is_valid():
            cartId = uuid.uuid4()
            serializer.validated_data['cartId'] = cartId
            itemNumber = int(serializer.validated_data['quantity'])
            for i in range(itemNumber):
                cartItem = CartItem()
                cartItem.cartId = cartId
                cartItem.itemId = serializer.validated_data['itemId']
                cartItem.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
