from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('upload/', views.upload_movie, name='upload_movie'),
    path('shorts/', views.shorts_dashboard, name='shorts_dashboard'),
    path('shorts/add/', views.add_short, name='add_short'),
    path('api/shorts/', views.shorts_analytics_api, name='shorts_analytics_api'),
]
