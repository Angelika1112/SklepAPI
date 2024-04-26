from django.contrib import admin #importujemy klasę admin z biblioteki django

from .models import Item, Category #importujemy klasy z utworzonych wcześniej modeli (Item i Category)
admin.site.register(Item) #rejestrujemy klasę "Item", aby była widoczna w panelu administratora
admin.site.register(Category) #rejestrujemy klasę "Category", aby była widoczna w panelu administratora

# Register your models here.
