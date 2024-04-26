from django.shortcuts import render
from .models import Category, Item #import wytworzonych wcześniej klas modeli
from .serializers import ItemSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def showItemList(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        itemList = Item.objects.all()
        serializer = ItemSerializer(itemList, many=True)
        return JsonResponse(serializer.data, safe=False)

# Create your views here.
