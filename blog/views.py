from blog.models import *
from pytils.translit import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post.html"
    context_object_name = 'post'


class BlogListView(ListView):
    model = Post
    template_name = "blog/blog.html"
    context_object_name = 'posts'
    queryset = Post.objects.filter(is_published=True)


class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ('post_name', 'containment',)
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.post_name)
            new_blog.save()
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ('post_name', 'containment',)

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', args=[self.kwargs.get('slug')])
