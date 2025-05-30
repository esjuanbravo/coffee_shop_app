from django.urls import path
from .views import MyOrder, CreateOrderProductView


urlpatterns=[
    path('orden/', MyOrder.as_view() , name='orders'),
    path('agregar-pedido/', CreateOrderProductView.as_view(), name='add_product')
]