from ..models import * #import wytworzonych wcześniej klas modeli
from ..serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

# Klasa zawierająca metody dotyczące kategorii
class CategoryApi(APIView):

    @swagger_auto_schema(responses={200: CategorySerializer, 400: 'Bad Request'},
                         operation_description='Operacja zwraca listę kategorii.')
    def get(self, request, format=None): # Metoda zwracająca listę kategorii produktów
        categoryList = Category.objects.all()

        serializer = CategorySerializer(categoryList, many=True)
        return Response(serializer.data)

# Klasa zawierająca metody dotyczące filtrowania produktów po kategorii
class CategoryApiDetail(APIView):

    @swagger_auto_schema(responses={200: ItemSerializer, 400: 'Bad Request'},
                         operation_description='Operacja zwraca listę produktów w podanej kategorii.')
    def get(self, request,categoryId):  # Metoda zwracająca listę produktów podanej kategorii
        item = Item.objects.filter(category=categoryId)
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)