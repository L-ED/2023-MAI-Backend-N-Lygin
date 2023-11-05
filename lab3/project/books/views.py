from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404
from .models import Book

# Create your views here.

def index(request):
    books_list = Book.objects.order_by('-publish_date')[:5]
    resp = {"latest_books_list":books_list}
    return render(request, "books/index.html", resp)


def get_books(request):

    pass


def book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "books/details.html", {"book": book})


def add_to_favorite(request):
    pass


def get_favorites(request):
    pass

