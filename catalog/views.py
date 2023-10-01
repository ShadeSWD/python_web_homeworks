from django.forms import inlineformset_factory
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version
from django.urls import reverse_lazy, reverse
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

    def get_success_url(self):
        return reverse('catalog:update', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['version_formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['version_formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy("catalog:list")

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=pk)
