from django.shortcuts import render
from .models import * #import wytworzonych wcześniej klas modeli
from .serializers import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import uuid
from drf_yasg.utils import swagger_auto_schema

class ItemApi(APIView):

    @swagger_auto_schema(responses={200: ItemSerializer}, operation_description='Operacja zwraca listę wszystkich przedmiotów')
    def get(self, request, format=None):
        itemList = Item.objects.all()

        serializer = ItemSerializer(itemList, many=True)
        return Response(serializer.data)

class ItemApiDetail(APIView):

    @swagger_auto_schema(responses={200: ItemDetailSerializer, 400: 'Bad Request'})
    def get(self, request,itemId):
        item = Item.objects.get(pk=itemId)
        serializer = ItemDetailSerializer(item)
        return Response(serializer.data)

class AdminItemsApi(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(responses={200: AdminItemSerializer, 400: 'Bad Request'})
    def get(self, request):
        itemList = Item.objects.all()
        serializer = AdminItemSerializer(itemList, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: AdminItemSerializer, 400: 'Bad Request'})
    def post(self, request, format=None):

        serializer = AdminItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminItemApiDetail(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(responses={200: AdminItemSerializer, 400: 'Bad Request'})
    def get(self, request,itemId):
        item = Item.objects.get(pk=itemId)
        serializer = AdminItemSerializer(item)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: AdminItemSerializer, 400: 'Bad Request'})
    def put(self, request,itemId):
        item = Item.objects.get(pk=itemId)
        serializer = AdminItemSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content', 400: 'Bad Request'})
    def delete(self, request, itemId, format=None):
        item = Item.objects.get(id=itemId)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryApi(APIView):

    @swagger_auto_schema(responses={200: CategorySerializer, 400: 'Bad Request'})
    def get(self, request, format=None):
        categoryList = Category.objects.all()

        serializer = CategorySerializer(categoryList, many=True)
        return Response(serializer.data)

class CategoryApiDetail(APIView):

    @swagger_auto_schema(responses={200: ItemSerializer, 400: 'Bad Request'})
    def get(self, request,itemId):
        item = Item.objects.filter(category=itemId)
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)

class CartTempClass:
    def __init__(self, cartId, itemlist):
        self.cartId = cartId
        self.itemList = itemlist
class CartApi(APIView):

    @swagger_auto_schema(responses={200: CartSerializer, 400: 'Bad Request'})
    def get(self, request,cartId):
        cartItemList = CartItem.objects.filter(cartId=cartId)
        item = CartTempClass(cartId,[cartItem.itemId for cartItem in cartItemList])
        serializer = CartSerializer(item)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: CartItemAddSerializer, 400: 'Bad Request'})
    def post(self, request, cartId):
        serializer = CartItemAddSerializer(data=request.data)
        if serializer.is_valid():
            itemNumber = int(serializer.validated_data['quantity'])
            for i in range(itemNumber):
                cartItem = CartItem()
                cartItem.cartId = cartId
                cartItem.itemId = serializer.validated_data['itemId']
                cartItem.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartEmptyApi(APIView):

    @swagger_auto_schema(responses={200: CartItemAddSerializer, 400: 'Bad Request'})

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