from django.urls import path
from catalog.views import ContactsListView, ProductsListView, ProductDetailView, BlogListView, PostCreateView,\
    PostUpdateView, PostDetailView

app_name = 'catalog'
urlpatterns = [
    path('', ProductsListView.as_view(), name='catalog_list'),
    path('contacts/', ContactsListView.as_view(), name='contacts_list'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('post/update/<slug>/', PostUpdateView.as_view(), name='post_update'),
    path('post/<slug>/', PostDetailView.as_view(), name='post_detail'),
]
