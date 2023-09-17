from django.contrib import admin
from contacts.models import Contacts


@admin.register(Contacts)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'country', 'itn', 'address')
    search_fields = ('itn', 'country')
