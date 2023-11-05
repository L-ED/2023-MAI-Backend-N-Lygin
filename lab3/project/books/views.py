from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from .models import Book
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = "books/index.html"
    context_object_name = "books_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Book.objects.order_by("-publish_date")


# def details(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)
#     return render(request, "books/details.html", {"book": book})


class DetailView(generic.DetailView):
    model = Book
    template_name = "polls/detail.html"


def vote(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.POST.get("Add_fav")== "Add to favorites":
        book.favorite = True
        book.save()
        return HttpResponseRedirect(reverse("books:details", args=(book.id,)))
    
    elif request.POST.get("return")== "back":
        return HttpResponseRedirect(reverse("books:results", args=(book.id,)))

