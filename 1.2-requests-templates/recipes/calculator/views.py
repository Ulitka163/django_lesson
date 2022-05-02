from django.http import HttpResponse
from django.shortcuts import render, reverse


def recipe(request):
    pages = {
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Бутерброд': reverse('buter')
    }
    context = {
        'pages': pages
    }
    return render(request, 'calculator/home.html', context)


def omlet(request):
    serving = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'яйца, шт': 2 * serving,
            'молоко, л': 0.1 * serving,
            'соль, ч.л.': 0.5 * serving,
        },
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    serving = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'макароны, г': 0.3 * serving,
            'сыр, г': 0.05 * serving,
        },
    }
    return render(request, 'calculator/index.html', context)


def buter(request):
    serving = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'хлеб, ломтик': 1 * serving,
            'колбаса, ломтик': 1 * serving,
            'сыр, ломтик': 1 * serving,
            'помидор, ломтик': 1 * serving,
        },
    }
    return render(request, 'calculator/index.html', context)


