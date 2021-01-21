from rest_framework import generics
from .import models
from .import serializers

class CategoriesList(generics.ListCreateAPIView):
    queryset = models.Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer
class CategoriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer

class MenusList(generics.ListCreateAPIView):
    queryset = models.Menus.objects.all()
    serializer_class = serializers.MenusSerializer
class MenusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Menus.objects.all()
    serializer_class = serializers.MenusSerializer

class ProfilesList(generics.ListCreateAPIView):
    queryset = models.Profiles.objects.all()
    serializer_class = serializers.ProfilesSerializer
class ProfilesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Profiles.objects.all()
    serializer_class = serializers.ProfilesSerializer
    
class SupplementsList(generics.ListCreateAPIView):
    queryset = models.Supplements.objects.all()
    serializer_class = serializers.SupplementsSerializer
class SupplementsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Supplements.objects.all()
    serializer_class = serializers.SupplementsSerializer