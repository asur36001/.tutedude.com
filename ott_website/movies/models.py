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
