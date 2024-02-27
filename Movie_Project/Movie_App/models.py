from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('Movie_App:mov_by_cat', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Movie(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    actors = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    release = models.DateField()
    link = models.URLField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('Movie_App:home', args=[self.category.slug, self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return '{}'.format(self.name)


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
