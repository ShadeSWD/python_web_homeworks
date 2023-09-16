from django.urls import path
from catalog.views import ContactsListView, ProductsListView, ProductDetailView

app_name = 'catalog'
urlpatterns = [
    path('', ProductsListView.as_view(), name='catalog'),
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product')
]
