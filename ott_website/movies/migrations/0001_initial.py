from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('genre', models.CharField(max_length=100)),
                ('release_year', models.PositiveIntegerField()),
                ('duration_minutes', models.PositiveIntegerField(help_text='Duration in minutes')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='posters/')),
                ('movie_file', models.FileField(upload_to='movies/')),
                ('is_featured', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={'ordering': ['-created_at']},
        ),
    ]
