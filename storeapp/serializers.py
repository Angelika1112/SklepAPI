from .models import Category, Item #import wytworzonych wcześniej klas modeli
from rest_framework import serializers #import klasy serializers z pakietu rest_framework

#Tworzymy klasę serializującą obiekty klasy 'Category'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

#Tworzymy klasę serializującą obiekty klasy 'Item'
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'category','name','quantity', 'price','imageUrl']