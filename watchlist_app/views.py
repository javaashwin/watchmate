from django.shortcuts import render
from watchlist_app.models import Watchlist
from watchlist_app.models import StreemingPlatform
from django.http import JsonResponse
#from .serializers import MovieSerializer
from .serializers import WatchlistSerializer
from .serializers import StreemingPlatSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


# Create your views here without serializer
# def movie_list(request):
#     movies=Movie.objects.all()
#     print(movies)
#     data={
#         'movies':list(movies.values())
#     }
#     print(list(movies.values()))
#     return JsonResponse(data)

# by using serializers and these are function based views
# @api_view(['GET','POST'])def movie_list(request):
# #     if(request.method=='GET'):
# #         movie=Movie.objects.all()
# #         serializer=MovieSerializer(movie,many=True)
# #         return Response(serializer.data)
# #     if request.method=='POST':
# #         serializer=MovieSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         else:
# #             return Response(serializer.errors)
#
#
# @api_view(['GET','PUT','DELETE'])
#
#
# def movie_details(request,id):
#
#     if(request.method=='GET'):
#         try:
#             movie = Movie.objects.get(pk=id)
#         except Movie.DoesNotExist:
#             return Response({'error':'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie, many=False)
#         return Response(serializer.data)
#     if request.method=='PUT':
#         movie = Movie.objects.get(pk=id)
#         serializer=MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     if(request.method=='DELETE'):
#         movie=Movie.objects.get(pk=id)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#CLASS BASED VIEWS

# class MovieList(APIView):
#     def get(self,request):
#         movies=Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
# class MovieDetails(APIView):
#     def get(self,request,id):
#         try:
#             movie = Movie.objects.get(pk=id)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie, many=False)
#         return Response(serializer.data)
#
#     def put(self,request,id):
#         movie = Movie.objects.get(pk=id)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     def delete(self,request,id):
#         movie = Movie.objects.get(pk=id)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def movie_list(request):
    if(request.method=='GET'):
        # movie=Watchlist.objects.get(title="pushpa")
        # movie = Watchlist.objects.filter(id__in=[1,7])
        movies = Watchlist.objects.all()
        #movie =Watchlist.objects.values('title','storyline')
        serializer=WatchlistSerializer(movies,many=True)
        return Response(serializer.data)





class WatchlistAV(APIView):
    def get(self,request):
        movies=Watchlist.objects.all()
        serializer = WatchlistSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailsAV(APIView):
    def get(self,request,id):
        try:
            movie = Watchlist.objects.get(pk=id)
        except Watchlist.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchlistSerializer(movie, many=False)
        return Response(serializer.data)

    def put(self,request,id):
        movie = Watchlist.objects.get(pk=id)
        serializer = WatchlistSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self,request,id):
        movie = Watchlist.objects.get(pk=id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreemingAV(APIView):
    def get(self,request):
        platforms=StreemingPlatform.objects.all()
        serializer = StreemingPlatSerializer(platforms, many=True,context={'request': request})
        return Response(serializer.data)

    def post(self,request):
        serializer = StreemingPlatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreemingDetailsAV(APIView):
    def get(self,request,id):
        try:
            platforms = StreemingPlatform.objects.get(pk=id)
        except StreemingPlatform.DoesNotExist:
            return Response({'error': ' not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreemingPlatSerializer(platforms, many=False,context={'request': request})
        return Response(serializer.data)

    def put(self,request,id):
        platforms = StreemingPlatform.objects.get(pk=id)
        serializer = StreemingPlatSerializer(platforms, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self,request,id):
        platforms = StreemingPlatform.objects.get(pk=id)
        platforms.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










