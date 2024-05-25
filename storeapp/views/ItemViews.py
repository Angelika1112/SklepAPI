from ..models import * #import wytworzonych wcześniej klas modeli
from ..serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

# Klasa zawierająca metody dotyczące produktów
class ItemApi(APIView):

    @swagger_auto_schema(responses={200: ItemSerializer},
                         operation_description='Operacja zwraca listę wszystkich produktów.')
    def get(self, request, format=None): # Metoda zwracająca listę produktów sklepu (z ograniczoną liczbą pól)
        itemList = Item.objects.all()

        serializer = ItemSerializer(itemList, many=True)
        return Response(serializer.data)

# Klasa zawierająca metody dotyczące konkretnego produktu
class ItemApiDetail(APIView):

    @swagger_auto_schema(responses={200: ItemDetailSerializer, 400: 'Bad Request'},
                         operation_description='Operacja zwraca szczegóły wybranego produktu.')
    def get(self, request,itemId): # Metoda zwracająca szczegóły wybranego produktu
        item = Item.objects.get(pk=itemId)
        serializer = ItemDetailSerializer(item)
        return Response(serializer.data)