from .models import * #import wytworzonych wcześniej klas modeli
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
        fields = ['id', 'category','name', 'price']

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'category','name','quantity', 'price','imageUrl']

class AdminItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id','category','name','quantity', 'price','imageUrl']

class CartItemAddSerializer(serializers.Serializer):
    cartId = serializers.CharField(allow_blank=True,required=False)
    itemId = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def validate(self, data):
        itemsInShop = Item.objects.get(id=data['itemId']).quantity
        if data['quantity'] > itemsInShop:
            raise serializers.ValidationError("Nie ma tylu produktów w sklepie, max "+str(itemsInShop))
        return data

class CartItemSerializer(serializers.Serializer):
    itemId = serializers.IntegerField()
    quantity = serializers.IntegerField()

class CartSerializer(serializers.Serializer):
    cartId = serializers.CharField(max_length=32, min_length=36)
    itemList = serializers.ListSerializer(child=serializers.IntegerField())

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderSummary
        fields = '__all__'
class OrderRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderSummary
        fields = ('firstName', 'lastName', 'city', 'street','homeNumber', 'zipCode','phoneNumber')