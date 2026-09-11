from django.contrib import messages
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MovieUploadForm, ShortVideoForm
from .models import Movie, ShortVideo


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


def shorts_dashboard(request):
    """Show creator-supplied YouTube analytics; this never plays videos or creates views."""
    shorts = ShortVideo.objects.all()
    totals = shorts.aggregate(
        views=Sum('views'), likes=Sum('likes'), comments=Sum('comments')
    )
    total_views = totals['views'] or 0
    total_likes = totals['likes'] or 0
    total_comments = totals['comments'] or 0
    return render(
        request,
        'movies/shorts_dashboard.html',
        {
            'shorts': shorts,
            'total_views': total_views,
            'total_likes': total_likes,
            'total_comments': total_comments,
            'engagement_rate': round(
                ((total_likes + total_comments) / total_views) * 100, 2
            ) if total_views else 0,
        },
    )


def add_short(request):
    if request.method != 'POST':
        return redirect('shorts_dashboard')

    form = ShortVideoForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Short added to your analytics dashboard.')
    else:
        messages.error(request, 'Could not add this Short. Check the fields and try again.')
    return redirect('shorts_dashboard')


def shorts_analytics_api(request):
    """Return stored, first-party metrics for a dashboard or future YouTube API sync."""
    shorts = ShortVideo.objects.all()
    return JsonResponse({
        'shorts': [
            {
                'id': short.id,
                'title': short.title,
                'youtube_url': short.youtube_url,
                'views': short.views,
                'likes': short.likes,
                'comments': short.comments,
                'engagement_rate': short.engagement_rate,
                'average_view_duration_seconds': short.average_view_duration_seconds,
                'last_synced_at': short.last_synced_at.isoformat(),
            }
            for short in shorts
        ]
    })
