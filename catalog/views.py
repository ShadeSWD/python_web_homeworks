from django.shortcuts import render
from catalog.models import *


def home(request):
    print(Product.objects.all()[:5])
    return render(request, "catalog/home.html")


def contacts(request):
    context = {
        'title': 'Contacts',
        'contact_info': Contacts.objects.first(),
    }

    if request.method == 'POST':
        visitor = dict()
        visitor['name'] = request.POST.get('name', None)
        visitor['phone'] = request.POST.get('phone', None)
        visitor['message'] = request.POST.get('message', None)
        print(visitor)
    return render(request, "catalog/contacts.html", context=context)
