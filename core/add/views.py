from django.shortcuts import render, redirect
from .models import Genre, Movie
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User

'''The @login_required(login_url="/login/") decorator ensures that
 views are accessible only to authenticated users. 
 If a non-authenticated user tries to access such a view, 
 they are redirected to "/login/" '''
@login_required(login_url="http://127.0.0.1:8000/login/")
def home(request):
    genres = Genre.objects.all()
    print(genres)
    context = {'genres': genres}
    print(context)
    return render(request, 'home.html', context)
 
@login_required(login_url="http://127.0.0.1:8000/login/")
def api_movies(request):
    movies_objs = Movie.objects.all()
    #filtering movies based on age-limit
    age = request.GET.get('age')
    if age:
        movies_objs = movies_objs.filter(age__lte=age)
         
    selected_genres = request.GET.getlist('genres')
    if selected_genres:
        movies_objs = movies_objs.filter(genres__name__in=selected_genres).distinct()

    movies_data = []
    for movie in movies_objs:
        movies_data.append({
            'movie_name': movie.movie_name,
            'movie_description': movie.movie_description,
            'age': movie.age,
            'movie_image': movie.movie_image.url,  # Assuming you have MEDIA_URL configured
            'genres': [genre.name for genre in movie.genres.all()]
        })
    
    '''returning an HTTP response with JSON content with safe flag 
    turned to false because payload is a list''' 
    return JsonResponse(movies_data, safe=False)
 
def login_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
             
            if not user_obj.exists():
                messages.error(request, "Username not found")
                return redirect('http://127.0.0.1:8000/login/')
             
            user_obj = authenticate(username=username, password=password)
             
            if user_obj:
                login(request, user_obj)
                return redirect('http://127.0.0.1:8000/home/')
             
            messages.error(request, "Wrong Password")
            return redirect('http://127.0.0.1:8000/login/')
             
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('http://127.0.0.1:8000/register/')
         
    return render(request, "login.html")
 
def register_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
             
            if user_obj.exists():
                messages.error(request, "Username is taken")
                return redirect('http://127.0.0.1:8000/register/')
             
            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
             
            messages.success(request, "Account created")
            return redirect('http://127.0.0.1:8000/login/')
         
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('http://127.0.0.1:8000/register/')
     
    return render(request, "register.html")
 
def custom_logout(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/login/')