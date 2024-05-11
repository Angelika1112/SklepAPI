from django.db import models # import klasy models z biblioteki Django

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

# Create your models here.
