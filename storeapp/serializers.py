from .models import * #import wytworzonych wcześniej klas modeli
from rest_framework import serializers #import klasy serializers z pakietu rest_framework

#Tworzymy klasę serializującą obiekty modelu 'Category'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

#Tworzymy klasę serializującą obiekty modelu 'Item' z ograniczoną liczbą pól
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'category','name', 'price']

#Tworzymy klasę serializującą obiekty modelu 'Item'
class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'category','name','quantity', 'price','imageUrl']

#Tworzymy klasę serializującą obiekty modelu 'Item' - dla admina (możliwa przyszła rozbudowa)
class AdminItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id','category','name','quantity', 'price','imageUrl']

#Tworzymy klasę serializującą zawierającą pola dotyczące produktu w koszyku
class CartItemAddSerializer(serializers.Serializer):
    cartId = serializers.CharField(allow_blank=True,required=False)
    itemId = serializers.IntegerField()
    quantity = serializers.IntegerField()

    # Nadpisanie metody walidującej dane żądania (błąd jeśli wybrano więcej produktów niż w sklepie )
    def validate(self, data):
        itemsInShop = Item.objects.get(id=data['itemId']).quantity
        if data['quantity'] > itemsInShop:
            raise serializers.ValidationError("Nie ma tylu produktów w sklepie, max "+str(itemsInShop))
        return data

#Tworzymy klasę serializującą zawierającą pola dotyczące pojedynczego rodzaju produktu sklepu
class CartItemSerializer(serializers.Serializer):
    itemId = serializers.IntegerField()
    quantity = serializers.IntegerField()

#Tworzymy klasę serializującą zawierającą pola dotyczące zawartości koszyka
class CartSerializer(serializers.Serializer):
    cartId = serializers.CharField(max_length=32, min_length=36)
    itemList = serializers.ListSerializer(child=serializers.IntegerField())

#Tworzymy klasę serializującą obiekty modelu 'OrderSummary'
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderSummary
        fields = '__all__'

#Tworzymy klasę serializującą obiekty modelu 'OrderSummary' ograniczone do danych teleadresowych
class OrderRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderSummary
        fields = ('firstName', 'lastName', 'city', 'street','homeNumber', 'zipCode','phoneNumber')