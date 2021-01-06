from django.urls import include, path

from movies.api import views

urlpatterns = [
    path('movies/', views.MovieListView.as_view(), name='movieList'),
    path('movies/create/', views.MovieCreateView.as_view(), name='movieDetails'),
    path('movies/<int:pk>', views.MovieRetrieveUpdateDestroyView.as_view(), name='movieDetails')
]

