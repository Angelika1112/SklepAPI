from django.contrib import admin #importujemy klasę admin z biblioteki django

from .models import Item, Category, CartItem, OrderSummary #importujemy klasy z utworzonych wcześniej modeli (Item i Category)
admin.site.register(Item) #rejestrujemy klasę "Item", aby była widoczna w panelu administratora
admin.site.register(Category) #rejestrujemy klasę "Category", aby była widoczna w panelu administratora
admin.site.register(CartItem) #rejestrujemy klasę "CartItem", aby była widoczna w panelu administratora
admin.site.register(OrderSummary) #rejestrujemy klasę "OrderSummary", aby była widoczna w panelu administratora

