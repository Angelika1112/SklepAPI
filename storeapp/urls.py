from django.urls import path
from . import views


urlpatterns = [
    path('itemki/',views.showItemList)
]
