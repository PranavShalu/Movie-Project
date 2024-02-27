from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'Movie_App'

urlpatterns = [
    path('', views.home, name='home'),
    path('/<slug:c_slug>/', views.home, name='mov_by_cat'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('movie/<int:movie_id>/addrating/', views.add_rating, name='add_rating'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('movie/<int:movie_id>/edit/', views.edit_movie, name='edit_movie'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
