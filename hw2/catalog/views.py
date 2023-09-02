from django.shortcuts import render


def home(request):
    return render(request, "catalog/home.html")


def contacts(request):
    if request.method == 'POST':
        visitor = dict()
        visitor['name'] = request.POST.get('name', None)
        visitor['phone'] = request.POST.get('phone', None)
        visitor['message'] = request.POST.get('message', None)
        print(visitor)
    return render(request, "catalog/contacts.html")
