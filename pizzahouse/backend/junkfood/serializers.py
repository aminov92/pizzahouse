from rest_framework import serializers

from .models import Categories
class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

from .models import Menus
class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = '__all__'

from .models import Profiles
class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = '__all__'

from .models import Supplements
class SupplementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplements
        fields = '__all__'