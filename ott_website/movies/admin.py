from django.contrib import admin
from .models import Movie, ShortVideo


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_year', 'duration_minutes', 'is_featured', 'created_at')
    list_filter = ('genre', 'release_year', 'is_featured')
    search_fields = ('title', 'genre')


@admin.register(ShortVideo)
class ShortVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'views', 'likes', 'comments', 'last_synced_at')
    search_fields = ('title', 'youtube_url')
