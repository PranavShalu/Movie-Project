from django import forms
from .models import Movie
from .models import Rating


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'category', 'actors', 'image', 'release', 'link', 'user', 'slug']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
