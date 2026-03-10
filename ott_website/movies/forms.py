from django import forms
from .models import Movie


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
