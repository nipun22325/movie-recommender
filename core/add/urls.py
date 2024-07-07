from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', views.custom_logout, name='logout'),
    path('api/movies', views.api_movies, name='api_movies'),
] 
