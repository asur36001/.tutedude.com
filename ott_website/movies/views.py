from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MovieUploadForm
from .models import Movie


def home(request):
    featured_movies = Movie.objects.filter(is_featured=True)[:6]
    all_movies = Movie.objects.all()
    return render(
        request,
        'movies/home.html',
        {'featured_movies': featured_movies, 'all_movies': all_movies},
    )


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})


def upload_movie(request):
    if request.method == 'POST':
        form = MovieUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movie uploaded successfully!')
            return redirect('home')
    else:
        form = MovieUploadForm()
    return render(request, 'movies/upload_movie.html', {'form': form})
