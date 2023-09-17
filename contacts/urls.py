from django.urls import path
from contacts.views import ContactsListView

app_name = 'contacts'

urlpatterns = [
    path('', ContactsListView.as_view(), name='list'),
]
