from django.urls import path,include
#from .views import MovieList,MovieDetails
from .views import WatchlistAV,WatchDetailsAV,StreemingAV,StreemingDetailsAV
from .views import movie_list
# urlpatterns = [
#     path('list/', movie_list),
#     path('<int:id>/',movie_details),
#     ]
#
# urlpatterns = [
#     path('list/', MovieList.as_view()),
#     path('<int:id>/',MovieDetails.as_view()),
#     ]


urlpatterns = [
    path('api/',movie_list),
    path('list/', WatchlistAV.as_view(),name='movie-list'),
    path('<int:id>/',WatchDetailsAV.as_view(),name='movie-detail'),
    path('stream/',StreemingAV.as_view(),name='stream-list'),
    path('stream/<int:id>/',StreemingDetailsAV.as_view(),name='streemingplatform-detail')
    ]
