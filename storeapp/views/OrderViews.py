from ..models import * #import wytworzonych wcześniej klas modeli
from ..serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
import collections

class OrderApi(APIView):

    @swagger_auto_schema(request_body=OrderRequestSerializer,
                         responses={201: OrderSerializer, 400: 'Bad Request'},
                         operation_description='Operacja finalizuje koszyk, generując dane zakończonego zamówienia.')
    def post(self, request, cartId):
        requestSerializer = OrderRequestSerializer(data=request.data)
        if requestSerializer.is_valid():
            cartItemList = CartItem.objects.filter(cartId=cartId)
            item = [cartItem.itemId for cartItem in cartItemList]
            itemCounter = collections.Counter(item)
            itemCounterDict = itemCounter.items()

            cartItemList.delete()

            totalPrice = 0
            for itemId, quantity in itemCounterDict:
                item = Item.objects.get(id=itemId)
                item.quantity-=quantity
                item.save()
                totalPrice += item.price * quantity

            order = OrderSummary()
            order.itemList = str(dict(itemCounter))
            order.itemList = order.itemList.replace(' ','')
            order.totalPrice = totalPrice
            order.firstName = requestSerializer.validated_data['firstName']
            order.lastName = requestSerializer.validated_data['lastName']
            order.city = requestSerializer.validated_data['city']
            order.street = requestSerializer.validated_data['street']
            order.homeNumber = requestSerializer.validated_data['homeNumber']
            order.zipCode = requestSerializer.validated_data['zipCode']
            order.phoneNumber = requestSerializer.validated_data['phoneNumber']

            order.save()
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(requestSerializer.data, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailApi(APIView):
    @swagger_auto_schema( responses={200: OrderSerializer, 400: 'Bad Request'},
                         operation_description='Operacja zwraca szczegóły wybranego zamówienia.')
    def get(self, request, orderId):
        order = OrderSummary.objects.get(id=orderId)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
