from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors', views.show_all_directors),
    path('directors/<int:id_dir>', views.show_one_director, name='directors_info'),
    path('actors', views.show_all_actors),
    path('actors/<int:id_act>', views.show_one_acter, name='actors_info'),

]