from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.shortcuts import redirect
from .forms import ProductsForms
from .models import Products

# class ProductsCreateView(generic.TemplateView):
#     template_name = 'product/all_product.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['product_form'] = ProductsForms()
#         return context
    
#     def post(self, request,):
#         product_form = ProductsForms(request.POST, request.FILES)
        
#         if 'product_submit' in request.POST and product_form.is_valid():
#             product_form.save()
#             return redirect('all_products')
        
        
        
#         return self.render_to_response({
#             'product_form': product_form,
#         })
    
class ProductListView(generic.ListView):
    model = Products
    template_name='product/list_product.html'
    context_object_name = 'products' 
    
    def get_queryset(self):
        return Products.objects.all().order_by('name')