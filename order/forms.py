from django.forms import ModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import OrderProduct


class OrderProductForm(ModelForm):
    class Meta:
        model = OrderProduct
        fields = ["product"]
