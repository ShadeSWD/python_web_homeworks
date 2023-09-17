from catalog.models import *
from django.views.generic import ListView, DetailView


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product.html"
    context_object_name = 'product'


class ProductsListView(ListView):
    model = Product
    template_name = "catalog/catalog.html"
    context_object_name = 'products'
    queryset = Product.objects.all()
