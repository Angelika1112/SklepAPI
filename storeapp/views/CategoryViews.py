from ..models import * #import wytworzonych wcześniej klas modeli
from ..serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

class CategoryApi(APIView):

    @swagger_auto_schema(responses={200: CategorySerializer, 400: 'Bad Request'},
                         operation_description='Operacja zwraca listę kategorii.')
    def get(self, request, format=None):
        categoryList = Category.objects.all()

        serializer = CategorySerializer(categoryList, many=True)
        return Response(serializer.data)

class CategoryApiDetail(APIView):

    @swagger_auto_schema(responses={200: ItemSerializer, 400: 'Bad Request'},
                         operation_description='Operacja zwraca listę produktów w podanej kategorii.')
    def get(self, request,categoryId):
        item = Item.objects.filter(category=categoryId)
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)