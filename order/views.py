from django.shortcuts import render
from django.views.generic import DetailView
from .models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class MyOrder(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'order/order.html'
    context_object_name = 'order'
    
    def get_object(self, queryset = None):
        return Order.objects.filter(is_active=True, user = self.request.user).first()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()
        
        total = sum(order_product.product.price * order_product.quantity for order_product in order.orderproduct_set.all())
        
        context['total'] = total
        return context