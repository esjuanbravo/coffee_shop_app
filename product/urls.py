from django.urls import path
from .views import  ProductListView

urlpatterns = [
    path('lista/', ProductListView.as_view(),name='list_products')
]
