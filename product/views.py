from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.shortcuts import redirect
from .forms import ProductsForms
from .models import Products, Category

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

# class ProductListView(generic.ListView):
#     model = Products
#     template_name='product/list_product.html'
#     context_object_name = 'products'

#     def get_queryset(self):
#         # Ordenamos por categoría y luego por nombre
#         return Products.objects.select_related('category').order_by('category__name', 'name')


class ProductListView(generic.ListView):
    model = Category  # Cambiamos el modelo a Category
    template_name = "product/list_product.html"
    context_object_name = "categories"  # Cambiamos el contexto a categorías

    def get_queryset(self):
        # Obtenemos categorías con sus productos relacionados y filtramos solo las con productos
        return (
            Category.objects.prefetch_related(
                "products_set"  # Nombre de la relación inversa (products_set por defecto)
            )
            .filter(products__isnull=False)
            .distinct()
            .order_by("name")
        )
