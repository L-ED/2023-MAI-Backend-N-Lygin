from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from .models import Book, Genre, Author
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.decorators.csrf import csrf_protect

# Create your views here.
class BookListView(generic.ListView):
    template_name = "books/index.html"
    context_object_name = "books_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Book.objects.order_by("-publish_date")
    

class AuthorListView(generic.ListView):
    template_name = "books/author_list.html"
    context_object_name = "author_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Author.objects.order_by("-date_of_birth")
    

class GenresListView(generic.ListView):
    template_name = "books/genre_list.html"
    context_object_name = "genre_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Genre.objects.all()

 
class FavoriteBooksView(LoginRequiredMixin, generic.ListView):
    template_name = "books/index.html"
    context_object_name = "books_list"
    model = Book

    def get_queryset(self) -> QuerySet[Any]:
        return Book.objects.filter(favorite_of=self.request.user)
    

# class GenreBooksView(generic.ListView):
#     template_name = "books/favorite.html"
#     model = Book

#     def get_queryset(self) -> QuerySet[Any]:
#         return Book.objects.filter(genre=self.request.user)


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "books/book_detail.html"


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = "books/author_detail.html"


class GenreDetailView(generic.DetailView):
    model = Genre
    template_name = "books/genre_detail.html"

@csrf_protect
@login_required
def vote(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=book_id)
        if request.POST.get("Add_fav")== "Add to favorites":
            book.favorite_of.add(request.user)
            book.save()
            return HttpResponseRedirect(reverse("books:book_detail", args=(book.id,)))
        
        elif request.POST.get("return")== "back":
            # return HttpResponseRedirect(reverse("", args=(book.id,)))
            return HttpResponseRedirect("/books")

