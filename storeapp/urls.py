from django.urls import path
from . import views


urlpatterns = [
    path('items/',views.ItemApi.as_view()),
    path('items/<int:itemId>/',views.ItemApiDetail.as_view()),
    path('categories/',views.CategoryApi.as_view()),
    path('categories/<int:itemId>/items/',views.CategoryApiDetail.as_view()),
    path('admin/items/',views.AdminItemsApi.as_view()),
    path('admin/items/<int:itemId>/',views.AdminItemApiDetail.as_view()),
    path('cart/<str:cartId>/',views.CartApi.as_view()),
    path('cart/',views.CartEmptyApi.as_view()),
]