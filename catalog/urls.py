from django.urls import path
from catalog.views import ProductsListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'catalog'

urlpatterns = [
    path('', ProductsListView.as_view(), name='list'),
    path('product/create/', ProductCreateView.as_view(), name='create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete'),
]
