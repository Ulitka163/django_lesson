from django.shortcuts import render, redirect

from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    books_objects = Book.objects.all()
    template = 'books/books_list.html'
    context = {
        'books': books_objects
    }
    return render(request, template, context)


def book_view(request, pub_date):
    books_objects = Book.objects.all()
    back_pub_date = Book.objects.exclude(pub_date__gte=pub_date).order_by('-pub_date').first()
    next_pub_date = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    print(back_pub_date, next_pub_date)
    book_list = []
    for book in books_objects:
        if str(book.pub_date) == pub_date:
            book_list.append(book)
    print(book_list)
    template = 'books/book.html'
    context = {
        'book_list': book_list,
        'back': back_pub_date,
        'next': next_pub_date,
    }
    return render(request, template, context)

