from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField(help_text='Duration in minutes')
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    movie_file = models.FileField(upload_to='movies/')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ShortVideo(models.Model):
    """A YouTube Short tracked in the creator's own analytics dashboard."""

    youtube_url = models.URLField(unique=True)
    title = models.CharField(max_length=200)
    published_at = models.DateTimeField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    average_view_duration_seconds = models.PositiveIntegerField(default=0)
    last_synced_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title

    @property
    def engagement_rate(self):
        if not self.views:
            return 0
        return round(((self.likes + self.comments) / self.views) * 100, 2)
