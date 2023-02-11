from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Sum, Max, Min, Count, Avg, Value

def show_all_movie(request):
    #movies = Movie.objects.order_by(F('year').asc(nulls_last=True),'-reting')
    movies = Movie.objects.annotate(true_bool=Value(True),
    false_bool=Value(False),
    str_field=Value('hello'),
    int_field=Value(5),
    new_budget=F('budget')+100,
    new_year=F('year')+F('reting')


)
    agg = movies.aggregate(Avg('budget'), Max('reting'), Min('reting'), Count('id'))

    return render(request,'movie_app/all_movies.html',{'movies':movies, 'agg': agg})



def show_one_movie(request,slug_movie:str):
    movie = get_object_or_404(Movie,slug=slug_movie)
    return render(request,'movie_app/one_movie.html',{'movies':movie, })


def show_all_directors(request):
    Directors = Director.objects.all()
    return render(request, 'movie_app/all_directors.html', {'Directors': Directors,})


def show_one_director(request,id_dir):
    director = get_object_or_404(Director, id=id_dir)
    return render(request,'movie_app/one_director.html',{'directors':director,})


def show_all_actors(request):
    Actors = Actor.objects.all()
    return render(request,'movie_app/all_actors.html', {'Actors':Actors} )

def show_one_acter(request, id_act):
    actor = get_object_or_404(Actor, id=id_act)
    return render(request,'movie_app/one_actor.html',{'actors':actor} )