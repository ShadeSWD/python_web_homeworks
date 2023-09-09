from django.shortcuts import render
from catalog.models import *


def home(request):
    context = {
        'title': 'Home',
        'products': Product.objects.all(),
    }

    if request.method == 'POST':
        product = request.POST.get('product', None)
        product()

    return render(request, "catalog/home.html", context=context)


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


def product(request, product_id):
    context = {
        'title': 'product page',
        'product': Product.objects.get(pk=product_id),
    }

    return render(request, "catalog/product.html", context=context)
