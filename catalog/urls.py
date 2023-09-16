from django.urls import path
from catalog.views import ContactsListView, ProductsListView, ProductDetailView, BlogListView, PostCreateView

app_name = 'catalog'
urlpatterns = [
    path('', ProductsListView.as_view(), name='catalog'),
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('post/create', PostCreateView.as_view(), name='post')
]
