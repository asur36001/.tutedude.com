# OTT Website with Django

This repository now includes a complete starter OTT website built with Django.

## Project location

- `ott_website/` - Django project root
- `movies` app handles movie upload, listing, and video playback

## Features

- Upload movies with title, description, genre, release year, duration, poster image, and video file
- Home page with featured movies and all movies
- Movie detail page with in-browser video player
- Django admin integration to manage movies
- Basic responsive dark-themed UI

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd ott_website
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Main routes

- `/` - Home page
- `/upload/` - Upload movie form
- `/movies/<id>/` - Movie detail and playback page
- `/admin/` - Admin panel
