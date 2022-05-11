from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phone_objects = Phone.objects.all()
    phone_dict = {}
    for p in phone_objects:
        phone_dict[p.id] = {'name': p.name,
                            'price': p.price,
                            'image': p.image,
                            'release_date': p.release_date,
                            'lte_exists': p.lte_exists,
                            'slug': p.slug
                            }
    template = 'catalog.html'
    context = phone_dict
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
