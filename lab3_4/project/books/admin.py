from django.contrib import admin
from .models import Book, Genre, Author
# Register your models here.
# admin.site.register(Book)
admin.site.register(Genre)

class BooksInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Administration object for Author models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields),
       grouping the date fields horizontally
     - adds inline addition of books in author view (inlines)
    """
    list_display = ('last_name',
                    'first_name', 'date_of_birth', )
    fields = ['first_name', 'last_name', 'date_of_birth',]
    inlines = [BooksInline]


class BookAdmin(admin.ModelAdmin):
    """Administration object for Book models.
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of book instances in book view (inlines)
    """
    list_display = ('title', 'author', 'get_genre', 'publish_date', 'get_favorite')
    fields =  ['title', 'author', 'genre', 'publish_date', 'favorite_of']


admin.site.register(Book, BookAdmin)
