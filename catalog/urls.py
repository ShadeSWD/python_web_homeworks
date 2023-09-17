from django.urls import path
from catalog.views import ProductsListView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('', ProductsListView.as_view(), name='list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail'),
]
