from ..models import * #import wytworzonych wcześniej klas modeli
from ..serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser
from drf_yasg.utils import swagger_auto_schema

# Klasa zawierająca metody dotyczące produktów - dla administratora
class AdminItemsApi(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(responses={200: AdminItemSerializer, 400: 'Bad Request'},
                         operation_description='Operacja zwraca listę wszystkich produktów wraz z szczegółami.')
    def get(self, request): # Metoda zwracająca wszystkie produkty z bazy
        itemList = Item.objects.all()
        serializer = AdminItemSerializer(itemList, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=AdminItemSerializer,
                         responses={200: AdminItemSerializer, 400: 'Bad Request'},
                         operation_description='Operacja dodaje nowy produkt.')
    def post(self, request, format=None):  # Metoda dodająca nowy produkt do bazy danych
        serializer = AdminItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Klasa zawierająca metody dotyczące konkretnego produktu - dla administratora
class AdminItemApiDetail(APIView):
    # Dodanie autoryzacji
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(responses={200: AdminItemSerializer, 400: 'Bad Request'},
                         operation_description='Operacja zwraca szczegóły wybranego produktu.')
    def get(self, request,itemId): # Metoda zwracająca konkretny produkt z bazy danych
        item = Item.objects.get(pk=itemId)
        serializer = AdminItemSerializer(item)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=AdminItemSerializer,
                         responses={200: AdminItemSerializer, 400: 'Bad Request'},
                         operation_description='Operacja modyfikuje wybrany produkt.')
    def put(self, request,itemId): # Metoda edytująca konkretny produkt z bazy danych
        item = Item.objects.get(pk=itemId)
        serializer = AdminItemSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content', 400: 'Bad Request'},
                         operation_description='Operacja usuwa wybrany produkt.')
    def delete(self, request, itemId, format=None):  # Metoda usuwająca konkretny produkt z bazy danych
        item = Item.objects.get(id=itemId)
        item.delete()
        return Response("Usunięto",status=status.HTTP_204_NO_CONTENT)
