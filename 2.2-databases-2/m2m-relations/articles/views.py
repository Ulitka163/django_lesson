from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    object_list = Article.objects.all().order_by('-published_at')
    template = 'articles/news.html'
    context = {'object_list': object_list}

    return render(request, template, context)
