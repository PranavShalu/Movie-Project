from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q, Avg
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MovieForm, RatingForm
from .models import Movie, Category, Rating
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.
def home(request, c_slug=None):
    # categories = Category.objects.all()
    # movies = Movie.objects.all()
    c_page = None
    movies_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        movies_list = Movie.objects.all().filter(category=c_page)
    else:
        movies_list = Movie.objects.all()
    return render(request, 'Home.html', {'movies': movies_list, 'categories': c_page})


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    ratings = Rating.objects.filter(movie=movie)
    average_rating = ratings.aggregate(Avg('rating'))['rating__avg']
    form = RatingForm(request.POST or None)
    if form.is_valid():
        rating = form.save(commit=False)
        rating.user = request.user
        rating.movie = movie
        rating.save()
        return redirect('detail', movie_id=movie.id)
    return render(request, "Detail.html", {'movie': movie, 'average_rating': average_rating, 'form': form})


@login_required()
def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.user != movie.user:
        return redirect('/')
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'Edit.html', {'form': form})


@login_required()
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.added_by = request.user
            movie.save()
            return redirect('/')
    else:
        form = MovieForm()
    return render(request, 'Add_Movie.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'Register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'Login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def search(request):
    query = request.GET.get('q')
    results = Movie.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'Search.html', {'movies': results})


def add_rating(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    form = RatingForm(request.POST or None)
    if form.is_valid():
        rating = form.save(commit=False)
        rating.user = request.user
        rating.movie = movie
        rating.save()
        return redirect('Movie_App:detail', movie_id=movie.id)
    return render(request, 'Rating.html', {'form': form})
