from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from .models import Order
from .forms import OrderProductForm
# Create your views here.


class MyOrder(LoginRequiredMixin, TemplateView):
    template_name = 'order/order.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = Order.objects.filter(is_active=True, user=self.request.user).first()
        context['order'] = order
        
        if order:
            total = sum(order_product.product.price * order_product.quantity for order_product in order.orderproduct_set.all())
        else:
            total = 0

        context['total'] = total
        return context
    
class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = 'order/create_order_product.html'
    form_class = OrderProductForm
    success_url = reverse_lazy('orders')
    
    # para validar el formulario 
    def form_valid(self, form):
        # el segundo parametro es un valor boleano para seber si se hizo en reguistro o no 
        order, _ = Order.objects.get_or_create(
            is_active= True,
            user=self.request.user
         )
        # hace instacia de de lo que se pide en la base de datos
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)
     