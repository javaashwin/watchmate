from rest_framework import serializers
#from .models import Movie
from .models import Watchlist
from .models import StreemingPlatform
from rest_framework import routers
# Normal Serializers
# def name_length(data):
#     if len(data)<2:
#         raise serializers.ValidationError("Name is too short")
#
# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[name_length])
#     description=serializers.CharField()
#     active=serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description= validated_data.get('description',instance.description)
#         instance.active= validated_data.get('active',instance.active)
#         instance.save()
#         return instance
#     # field level validation
#     def validate_name(self,value):
#         if len(value)<3:
#             raise serializers.ValidationError("Name is too short")
#
#         else:
#             return value
#
#     # Object level validation
#     def validate(self,data):
#         if data['name']==data['description']:
#             raise serializers.ValidationError("Name and desc should not be same")
#         else:
#             return data


#MODEL SERIALIZERS

# class MovieSerializer(serializers.ModelSerializer):
#     # length_of_name = serializers.SerializerMethodField()
#     class Meta:
#         model = Movie
#    #    fields = "__all__"
#    #    fields=['id','name','description']
#         exclude=['active']


# CUSTOM MODEL SERIALIZER
    # def get_length_of_name(self,obj):
    #     return len(obj.name)

# VALIDATIONS ARE SHOWN HERE
    # def validate_name(self, value):
    #     if len(value) < 3:
    #         raise serializers.ValidationError("Name is too short")
    #
    #     else:
    #         return value
    #
    # def validate(self,data):
    #     if data['name']==data['description']:
    #         raise serializers.ValidationError("Name and desc should not be same")
    #     else:
    #         return data



class WatchlistSerializer(serializers.ModelSerializer):
    # length_of_name = serializers.SerializerMethodField()
    class Meta:
        model = Watchlist
        fields = "__all__"
   #    fields=['id','name','description']
     #   exclude=['active']


class StreemingPlatSerializer(serializers.ModelSerializer):
    # watchlist = WatchlistSerializer(many=True, read_only=True)
    # # watchlist = serializers.HyperlinkedRelatedField(
    # #     many=True,
    # #     read_only=True,
    # #     view_name='movie-detail')

    class Meta:
        model = StreemingPlatform
        fields="__all__"

    #

    watchlist = serializers.StringRelatedField(many=True)

