from django.urls import path
from . import views

app_name="books"
urlpatterns = [
    path("", views.BookListView.as_view(), name="books"),
    path("<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("<int:book_id>/vote/", views.vote, name="vote"),
    path("favorites/", views.FavoriteBooksView.as_view(), name="favorites")
]

urlpatterns+=[
    path("authors/", views.AuthorListView.as_view(), name="authors"),
    path("authors/<int:pk>/", views.AuthorDetailView.as_view(), name="author-details")
]