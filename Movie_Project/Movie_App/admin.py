from django.contrib import admin
from .models import Movie, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'release', 'actors', 'user', 'description', 'image', 'link']
    search_fields = ['name', 'release']
    list_filter = ['category', 'name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Movie, MovieAdmin)
