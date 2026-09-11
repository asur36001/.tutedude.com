from django import forms
from .models import Movie, ShortVideo


class MovieUploadForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            'title',
            'description',
            'genre',
            'release_year',
            'duration_minutes',
            'poster',
            'movie_file',
            'is_featured',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class ShortVideoForm(forms.ModelForm):
    class Meta:
        model = ShortVideo
        fields = [
            'youtube_url',
            'title',
            'published_at',
            'views',
            'likes',
            'comments',
            'average_view_duration_seconds',
        ]
        widgets = {
            'published_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
