from django.forms import formset_factory
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
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
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    success_url = reverse_lazy("catalog:list")

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=pk)

    def form_valid(self, form):
        new_product = form.save()
        new_product.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy("catalog:list")

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=pk)
