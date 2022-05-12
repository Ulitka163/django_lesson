from django.shortcuts import render

from books.models import Book


def books_view(request):
    books_objects = Book.objects.all()
    template = 'books/books_list.html'
    context = {
        'books': books_objects
    }
    return render(request, template, context)
