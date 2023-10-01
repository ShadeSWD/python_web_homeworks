from django.urls import path
from blog.views import BlogListView, PostCreateView, PostUpdateView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('post/create', PostCreateView.as_view(), name='create'),
    path('post/<slug>/', PostDetailView.as_view(), name='detail'),
    path('post/<slug>/update/', PostUpdateView.as_view(), name='update'),
]
