from catalog.models import *
from catalog.forms import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product.html"
    context_object_name = 'product'


class ProductsListView(ListView):
    model = Product
    template_name = "catalog/catalog.html"
    context_object_name = 'products'
    queryset = Product.objects.all()


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = '/catalog'

    def form_valid(self, form):
        new_product = form.save()
        new_product.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    pass


class ProductDeleteView(DeleteView):
    pass
