from django.urls import path
from .views import MyOrder
urlpatterns=[
    path('orden/', MyOrder.as_view() , name='orders')
]