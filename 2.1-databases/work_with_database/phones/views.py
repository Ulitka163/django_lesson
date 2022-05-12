from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_ = request.GET.get('sort')
    if sort_ == 'name':
        phone_objects = Phone.objects.order_by('name')
    elif sort_ == 'max_price':
        phone_objects = Phone.objects.order_by('-price')
    elif sort_ == 'min_price':
        phone_objects = Phone.objects.order_by('price')
    else:
        phone_objects = Phone.objects.all()
    template = 'catalog.html'
    context = {
        'phones': phone_objects
    }
    return render(request, template, context)


def show_product(request, slug):
    phone_objects = Phone.objects.all()
    for phone in phone_objects:
        if phone.slug == slug:
            template = 'product.html'
            context = {
                'phone': phone
            }
            return render(request, template, context)
