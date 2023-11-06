from django.urls import path, re_path
from . import views

app_name="books"
urlpatterns = [
    path("", views.BookListView.as_view(), name="books"),
    path("<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("<int:book_id>/vote/", views.vote, name="vote"),
    path("favorites/", views.FavoriteBooksView.as_view(), name="favorites"),
    # re_path(r"search\?q=(?P<quiery_string>[0-9A-Za-z]+)?$", views.search, name='search'),
    re_path(r"^search/$", views.search, name='search'),
    # path("search?q=<str:quiery_string>)", views.search, name='search'),
]

urlpatterns+=[
    path("authors/", views.AuthorListView.as_view(), name="authors"),
    path("authors/<int:pk>/", views.AuthorDetailView.as_view(), name="author-details"),
    path("genres/", views.GenresListView.as_view(), name="genres"),
    path("genres/<int:pk>/", views.GenreDetailView.as_view(), name="genre-details"),
]