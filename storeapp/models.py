from django.db import models # import klasy models z biblioteki Django
import uuid

# tworzenie klasy "Category"
class Category(models.Model):
    id = models.AutoField(primary_key=True) #dodanie pola numerycznego "id"
    name = models.CharField(max_length=25) #dodanie pola nazwy
    def __str__(self):
        return self.name


# tworzenie klasy "Item"
class Item(models.Model):
    id = models.AutoField(primary_key=True) #dodanie pola numerycznego "id"
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #dodanie pola zawierającego referencję do kategorii
    name = models.CharField(max_length=25) #dodanie pola nazwy
    quantity = models.IntegerField(default=0) #dodanie pola z ilością produktów
    price = models.DecimalField(max_digits = 5, decimal_places = 2) #dodanie pola z ceną produktu
    imageUrl = models.CharField(max_length=200) #dodanie pola zawierającego odnośnik do zdjęcia produktu
    def __str__(self):
        return self.name

# tworzenie klasy "CartItem" zawierającej id koszyka oraz id produktu
class CartItem(models.Model):
    cartId = models.CharField(max_length=36)
    itemId = models.IntegerField(default=0)

# tworzenie klasy "OrderSummary" zawierającej dane podsumowania zamówienia
class OrderSummary(models.Model):
    id = models.AutoField(primary_key=True)
    itemList = models.CharField(max_length=200)
    totalPrice = models.DecimalField(max_digits = 5, decimal_places = 2)
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=25)
    homeNumber = models.CharField(max_length=10)
    zipCode = models.CharField(max_length=6)
    phoneNumber = models.CharField(max_length=9)
