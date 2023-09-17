from contacts.models import *
from django.views.generic import ListView


class ContactsListView(ListView):
    model = Contacts
    template_name = "contacts/contacts.html"
    context_object_name = 'contact'
    queryset = Contacts.objects.first()
