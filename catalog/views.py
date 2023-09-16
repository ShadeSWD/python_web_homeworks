from catalog.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product.html"
    context_object_name = 'product'


class PostDetailView(DetailView):
    model = Post
    template_name = "catalog/post.html"
    context_object_name = 'post'


class ContactsListView(ListView):
    model = Contacts
    template_name = "catalog/contacts.html"
    context_object_name = 'contact'
    queryset = Contacts.objects.first()


class BlogListView(ListView):
    model = Post
    template_name = "catalog/blog.html"
    context_object_name = 'posts'
    queryset = Post.objects.all()


class PostCreateView(CreateView):
    model = Post
    template_name = "catalog/post_form.html"
    fields = ('post_name', 'slug', 'containment', 'theme')
    success_url = reverse_lazy('post_list:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.save()
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    template_name = "catalog/post_form.html"
    fields = ('post_name', 'containment', 'theme')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail:detail', args=[self.kwargs.get('slug')])


class ProductsListView(ListView):
    model = Product
    template_name = "catalog/catalog.html"
    context_object_name = 'products'
    queryset = Product.objects.all()
