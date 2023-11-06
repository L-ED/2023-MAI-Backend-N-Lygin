from django.db import models
from django.urls import reverse
from django.conf import settings


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    genre = models.ManyToManyField(Genre)
    publish_date = models.DateTimeField("publish date")
    favorite_of = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self) -> str:
        return f"{self.title}"
    

    def get_genre(self):
        return ", ".join(genre_.username for genre_ in self.genre.all())


    def get_favorite(self):
        return ", ".join(fav.name for fav in self.favorite_of.all())

# class User(models.Mode)