from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from .models import Book
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = "books/index.html"
    context_object_name = "books_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Book.objects.order_by("-publish_date")


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Book
    template_name = "books/detail.html"
    

@login_required
def vote(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.POST.get("Add_fav")== "Add to favorites":
        book.favorite = True
        book.save()
        return HttpResponseRedirect(reverse("books:detail", args=(book.id,)))
    
    elif request.POST.get("return")== "back":
        # return HttpResponseRedirect(reverse("", args=(book.id,)))
        return HttpResponseRedirect("/books")

