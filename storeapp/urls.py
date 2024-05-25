from django.urls import path
from . import views

# Endpointy API - kierujące do konkretnych widoków
urlpatterns = [
    path('items/',views.ItemApi.as_view()), # Widoki produktów
    path('items/<int:itemId>/',views.ItemApiDetail.as_view()), # Widoki szczegółów produktu
    path('categories/',views.CategoryApi.as_view()), # Widoki kategorii
    path('categories/<int:categoryId>/items/',views.CategoryApiDetail.as_view()), # Widoki filtrowania produktów
    path('admin/items/',views.AdminItemsApi.as_view()), # Widoki administratora - produkty
    path('admin/items/<int:itemId>/',views.AdminItemApiDetail.as_view()), # Widoki administratora - szczegóły produktu
    path('cart/',views.CartEmptyApi.as_view()), # Widoki koszyka
    path('cart/<str:cartId>/',views.CartApi.as_view()), # Widoki konkretnego koszyka
    path('cart/<str:cartId>/order',views.OrderApi.as_view()), # Widoki finalzacji zamówienia
    path('order/<int:orderId>',views.OrderDetailApi.as_view()), # Widoki zamówień
]