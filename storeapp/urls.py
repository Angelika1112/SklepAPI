from django.urls import path
from . import views


urlpatterns = [
    path('items/',views.ItemApi.as_view()),
    path('items/<int:itemId>/',views.ItemApiDetail.as_view()),
    path('admin/items/',views.AdminItemsApi.as_view()),
    path('admin/items/<int:itemId>/',views.AdminItemApiDetail.as_view()),
]